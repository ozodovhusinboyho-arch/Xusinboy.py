# Name
name = input("What is your name: ")

# Inputs (converted to float for numeric operations)
how_much_is_Monthly_net_income = float(input("How much is Monthly net income: "))
how_much_are_Fixed_expenses = float(input("How much are Fixed expenses (Rent, utilities, etc.): "))
Variable_expenses = float(input("How much are Variable expenses: ")) 
Current_savings_amount = float(input('How much is Current savings amount: ')) 
Apartment_down_payment_goal = float(input('How much is Apartment down payment goal: '))
Months_until_desired_purchase = float(input('How many months until desired purchase: ')) 

# Total monthly expenses (sum of fixed + variable)
Total_monthly_expenses = how_much_are_Fixed_expenses + Variable_expenses

# Monthly savings (income - expenses)
Monthly_savings = how_much_is_Monthly_net_income - Total_monthly_expenses

# Savings rate percentage
Savings_rate_percentage = (Monthly_savings / how_much_is_Monthly_net_income) * 100

# Projected savings after target months
Projected_savings_after_target_months = Monthly_savings * Months_until_desired_purchase

# Total projected amount (current + projected)
Total_projected_amount = Current_savings_amount + Projected_savings_after_target_months

# Monthly savings needed to reach goal
Monthly_savings_needed_to_reach_goal = Apartment_down_payment_goal / Months_until_desired_purchase

# Additional monthly savings needed
Additional_monthly_savings_needed = Monthly_savings_needed_to_reach_goal - Monthly_savings

# Financial Health Indicators
Critical_warning = Total_monthly_expenses >= how_much_is_Monthly_net_income
print(f"Critical warning: {Critical_warning}")

Below_recommended = Savings_rate_percentage < 20
print(f"Below recommended (<20%): {Below_recommended}")

Good_position = 20 <= Savings_rate_percentage < 30
print(f"Good position (20-29%): {Good_position}")

Excellent_position = Savings_rate_percentage >= 30
print(f"Excellent position (≥30%): {Excellent_position}")

Goal_achievable = Total_projected_amount >= Apartment_down_payment_goal
print(f"Goal achievable: {Goal_achievable}")
