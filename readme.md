# Company-wide Expense Tracking System: Development Assignment

<img src="./assets/budget.webp" alt="Expense Tracking System Assignment" width="500">


## Assignment Brief
As the Data Manager, I am tasking you with developing a critical financial management tool for our organization. We need a robust, automated system to track and report on company card expenses across all departments. This system will be used by all managers who have company cards, enabling them to monitor their team's spending against allocated budgets efficiently.

Your assignment is to create a Python-based application that will:
1. Automatically process monthly transaction data from company cards
2. Generate comprehensive spending reports, including visual representations of expenses
3. Compare actual spending against predetermined budgets
4. Distribute these reports via email to respective managers and the finance department

This tool is crucial for maintaining financial discipline, identifying spending patterns, and making informed budgetary decisions across the company. Your work will directly impact our organization's financial health and decision-making processes.

## Key Objectives
- Develop a scalable solution that can handle multiple users and varying budget amounts
- Ensure the system is user-friendly, requiring minimal manual input from managers
- Implement strong security measures to protect sensitive financial data
- Create clear, insightful reports that aid in quick decision-making

Please refer to the detailed requirements below for specific functionalities and technical specifications. The deadline for the initial prototype is [Insert Date], with a company-wide rollout planned for [Insert Date].

This project is a high priority for the finance department, and your expertise is crucial to its success. Regular progress updates will be expected, and don't hesitate to reach out if you need any clarifications or resources.

## Requirements

### 1. Data Handling
- Read transaction data from a CSV file named 'monthly_company_card_transactions.csv'
- CSV columns should include: Date, Description, Amount, Category
- Parse dates and handle numerical data appropriately

### 2. Analysis
- Calculate total spending for the month
- Compare spending to the monthly budget of $5,000
- Group and sum spending by category
- Identify the top 5 individual expenses

### 3. Visualization
- Create a pie chart showing the percentage of spending in each category
- Save the chart as an image file

### 4. Reporting
- Generate a text report including:
  - Reporting period
  - Total spent vs. budget
  - Remaining budget
  - Percentage of budget spent
  - Breakdown of spending by category
  - Top 5 expenses
  - Budget status (over/under budget)

### 5. Email Functionality
- Compose an email with the text report in the body
- Attach the pie chart image to the email
- Send the email to a specified address

### 6. Security
- Use environment variables or a secure method to store email credentials
- Do not hardcode sensitive information in the script

## Hints and Tips
1. Use pandas for data manipulation and analysis
2. matplotlib is great for creating the pie chart
3. Look into Python's built-in `email` and `smtplib` modules for sending emails
4. Consider using `datetime` for handling dates
5. Store the pie chart in memory using `BytesIO` before attaching to the email

## Learning Resources
1. Pandas documentation: https://pandas.pydata.org/docs/
2. Matplotlib tutorials: https://matplotlib.org/stable/tutorials/index.html
3. Python's email modules: https://docs.python.org/3/library/email.html
4. smtplib documentation: https://docs.python.org/3/library/smtplib.html
5. Real Python's guide on sending emails: https://realpython.com/python-send-email/
6. Tutorial on working with CSV files in Python: https://realpython.com/python-csv/

## Bonus Challenges
- Implement error handling and logging
- Add command-line arguments to specify the input file and output email address
- Create a config file for easily adjustable settings (budget amount, email addresses, etc.)
- Generate additional visualizations (e.g., a bar chart of spending over time)

## Deliverables
1. Python script that accomplishes all the above requirements
2. A brief README explaining how to set up and run the script
3. Any necessary requirements file (e.g., requirements.txt)

Good luck, and don't hesitate to ask for clarification on any part of the project!