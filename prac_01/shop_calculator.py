def main():
    num_items = int(input("Number of items: "))
    while num_items < 1:
        print("Invalid number of items!")
        num_items = int(input("Number of items: "))
    item_list = []
    for i in range(0, num_items, 1):
        item = float(input("Price of item: "))
        item_list.append(item)
    total_cost = str(sum(item_list))
    print("Total price for", num_items, "item(s) is $" + total_cost)

    # TODO Rewrite without list

    num_items = int(input("Number of items: "))
    item_price_total = 0
    while num_items < 1:
        print("Invalid number of items!")
        num_items = int(input("Number of items: "))
    for i in range(0, num_items, 1):
        item = float(input("Price of item: "))
        item_price_total = item_price_total + item
    print("Total price for", num_items, "item(s) is $" + str(item_price_total))


main()