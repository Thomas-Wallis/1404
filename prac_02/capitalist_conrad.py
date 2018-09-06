def main():
    import random
    stock_value = 10
    day_counter = 1
    print("Starting price: ${}".format(stock_value))
    while stock_value >= 0.01 and stock_value <= 1000:
        stock_change_determine = random.randint(1, 2)
        stock_change_positive = random.uniform(0,10)
        stock_change_negative = random.uniform(0, 5)
        if stock_change_determine == 1:
            stock_value = stock_value + (stock_change_positive / 100 * stock_value)
        else:
            stock_value = stock_value - (stock_change_negative / 100 * stock_value)
        day_counter += 1
        print("On day {} price is: ${:,.2f}".format(day_counter, stock_value))


main()