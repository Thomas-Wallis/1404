TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

Tarriff = 0
print("Electricity bill estimator 2.0")
while Tarriff is not TARIFF_11 and Tarriff is not TARIFF_31:
    Tarriff = int(input("Which tarriff? 11 or 31: "))
    if Tarriff == 11:
        Tarriff = TARIFF_11
    elif Tarriff == 31:
        Tarriff = TARIFF_31
    else:
        print("Please select a valid tarriff.")
daily_use = float(input("Daily use in kWh: "))
billing_days = float(input("Number of days in the billing period: "))
bill_estimate = Tarriff * daily_use * billing_days
print("Estimated bill: ${:,.2f}".format(bill_estimate))