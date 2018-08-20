"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = 0
while sales >= 0:
    sales = float(input("Enter sales here:"))
    if sales >= 1000:
        bonus = sales * 0.15
    elif sales > 0 and sales < 1000:
        bonus = sales * 0.1
    elif sales < 0:
        bonus = 0
    else:
        bonus = 0
    print(bonus)

# TODO Learn while loop patterns Chapter 2 [Finished]