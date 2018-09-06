def main():
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


main()