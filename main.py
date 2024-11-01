import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def load_data(file_path):
    """Load and process the CSV data"""
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def calculate_budget_summary(df, monthly_budget=5000):
    """Calculate budget-related metrics"""
    total_spent = abs(df['Amount'].sum())
    remaining_budget = monthly_budget - total_spent
    percent_spent = (total_spent / monthly_budget) * 100
    
    # Group spending by category
    category_spending = df.groupby('Category')['Amount'].sum().abs()
    
    # Get top 5 expenses
    top_expenses = df.sort_values('Amount', key=lambda x: abs(x)).tail(5)[['Date', 'Description', 'Amount']]
    
    return {
        'total_spent': total_spent,
        'remaining_budget': remaining_budget,
        'percent_spent': percent_spent,
        'category_spending': category_spending,
        'top_expenses': top_expenses
    }

def create_pie_chart(category_spending):
    """Create and save pie chart of spending by category"""
    plt.figure(figsize=(10, 8))
    plt.pie(category_spending, labels=category_spending.index, autopct='%1.1f%%')
    plt.title('Expenses by Category')
    
    # Save to BytesIO object
    img_data = BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    plt.close()
    
    return img_data

def create_text_report(summary):
    """Generate formatted text report"""
    report = f"""Expense Report Summary

Reporting Period: January 2024

Budget Overview:
---------------
Total Budget: ${5000:,.2f}
Total Spent: ${summary['total_spent']:,.2f}
Remaining Budget: ${summary['remaining_budget']:,.2f}
Percentage of Budget Spent: {summary['percent_spent']:.1f}%

Category Breakdown:
-----------------
"""
    
    for category, amount in summary['category_spending'].items():
        report += f"{category}: ${abs(amount):,.2f}\n"
    
    report += "\nTop 5 Expenses:\n--------------\n"
    for _, row in summary['top_expenses'].iterrows():
        report += f"{row['Date'].strftime('%Y-%m-%d')} - {row['Description']}: ${abs(row['Amount']):,.2f}\n"
    
    report += f"\nBudget Status: {'OVER BUDGET' if summary['total_spent'] > 5000 else 'Under Budget'}"
    
    return report

def send_email(report_text, chart_data):
    """Send email with report and chart"""
    sender_email = os.getenv('EMAIL_ADDRESS')
    sender_password = os.getenv('APP_PASSWORD')
    
    if not sender_email or not sender_password:
        raise ValueError("Missing EMAIL_ADDRESS or APP_PASSWORD in .env file")
        
    receiver_email = os.getenv('RECEIVER_EMAIL')
    
    # Create message
    msg = MIMEMultipart()
    msg['Subject'] = 'Monthly Expense Report - January 2024'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # Add text report
    msg.attach(MIMEText(report_text, 'plain'))
    
    # Add pie chart
    img = MIMEImage(chart_data.getvalue())
    img.add_header('Content-ID', '<expense_chart>')
    msg.attach(img)
    
    try:
        # Send email using SSL context
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
    except Exception as e:
        print(f"Detailed error: {str(e)}")
        raise

def main():
    # Load and process data
    df = load_data('data/october-2024.csv')
    
    # Calculate summary
    summary = calculate_budget_summary(df)
    
    # Create pie chart
    chart_data = create_pie_chart(summary['category_spending'])
    
    # Generate report
    report_text = create_text_report(summary)
    
    # Send email
    try:
        send_email(report_text, chart_data)
        print("Report sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    main()