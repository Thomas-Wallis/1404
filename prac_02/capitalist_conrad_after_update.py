def main():
    import random
    stock_value = 10
    day_counter = 1
    out_file = open("OUTPUT_FILE.txt","w")
    print("Starting price: ${}".format(stock_value), file=out_file)
    while stock_value >= 1 and stock_value <= 100:
        stock_change_determine = random.randint(1, 2)
        stock_change_positive = random.uniform(0,17.5)
        stock_change_negative = random.uniform(0, 5)
        if stock_change_determine == 1:
            stock_value = stock_value + (stock_change_positive / 100 * stock_value)
        else:
            stock_value = stock_value - (stock_change_negative / 100 * stock_value)
        day_counter += 1
        print("On day {} price is: ${:,.2f}".format(day_counter, stock_value), file=out_file)
    out_file.close()


main()