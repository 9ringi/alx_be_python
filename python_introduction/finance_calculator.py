# finance_calculator.py

# User Input for Financial Details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses

# Project Annual Savings
interest_rate = 0.05  # Assume a simple annual interest rate of 5%
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)

# Output Results
print(f"Your monthly savings are ${monthly_savings:.2f}")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}")
