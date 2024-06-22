#5. Personal Finance Calculator

#User Input for Financial Details:
income = float(input("Enter your monthly income: "))
expense = float(input("Enter your total monthly expenses: "))
#Calculate Monthly Savings:
Monthly_Savings = income - expense
#Project Annual Savings:
interest_rate = 0.05 #Assume a simple annual interest rate of 5%.
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * interest_rate)

#Output Results:
print("Your monthly savings are", Monthly_Savings)
print("Projected savings after one year, with interest, is:", Projected_Savings)