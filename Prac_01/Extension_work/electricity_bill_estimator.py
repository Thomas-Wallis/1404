print("Electricity bill estimator")
price = int(input("Enter cents per kWh: "))
daily_use = float(input("Daily use in kWh: "))
billing_days = float(input("Number of days in the billing period: "))
bill_estimate = price * daily_use * billing_days
print("Estimated bill: ${:,.2f}".format(bill_estimate))