import sqlite3
from datetime import datetime

def generate_final_report(username):
    conn = sqlite3.connect('finance_manager.db')
    cursor = conn.cursor()

    # Retrieve user_id based on the provided username
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    if not user:
        print("User not found.")
        return

    user_id = user[0]

    cursor.execute("SELECT amount, description, date FROM income WHERE user_id = ?", (user_id,))
    income_data = cursor.fetchall()

    cursor.execute("SELECT amount, description, date FROM expenses WHERE user_id = ?", (user_id,))
    expenses_data = cursor.fetchall()

    total_income = sum([income[0] for income in income_data])
    total_expenses = sum([expense[0] for expense in expenses_data])
    balance = total_income - total_expenses
    
    report = {
    "username": username,
    "report_date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    "income": [
        {"description": income[1], "amount": income[0], "date": income[2]}
        for income in income_data
    ],
    "total_income": total_income,
    "expenses": [
        {"description": expense[1], "amount": expense[0], "date": expense[2]}
        for expense in expenses_data
    ],
    "total_expenses": total_expenses,
    "balance": balance
        }

# To display the same output as before, you can use the following code:
    print("Final Financial Report for", report["username"])
    print("=" * 50)
    print("Income:")
    for income in report["income"]:
        print(f"- {income['description']}: {income['amount']} on {income['date']}")
    print(f"Total Income: {report['total_income']}\n")

    print("Expenses:")
    for expense in report["expenses"]:
        print(f"- {expense['description']}: {expense['amount']} on {expense['date']}")
    print(f"Total Expenses: {report['total_expenses']}\n")

    print("=" * 50)
    print(f"Balance: {report['balance']}")
    print("=" * 50)
    print(f"Report generated on: {report['report_date']}")

    conn.close()

    return report


# Example usage
# username = "sikander"  # Replace with the actual username
# report = generate_final_report('shri')
# print(report)
# for income in report['income']:
#     print(income['amount'])
