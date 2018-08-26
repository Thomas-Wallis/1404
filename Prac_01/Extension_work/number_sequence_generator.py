from math import sqrt
even_numbers = []
odd_numbers = []
square_numbers = []
menu = input("Number Generator \n(C)hoose numbers: \n(F)inish: \n>>>").upper()
while menu != "F":
    if menu == "C":
        while menu == "C":
            try:
                number_one = int(input("Choose the first number please:"))
                if number_one < 0:
                    print("Number must be at least 0")
                else:
                    while number_one > -1:
                        try:
                            number_two = int(input("Choose the second number please:"))
                            if number_two <= number_one:
                                print("The second number must be greater than the first")
                            else:
                                #print("All the even numbers between {} and {} are: ".format(number_one, number_two))
                                for number in range(number_one, number_two + 1):
                                    if number % 2 == 0:
                                        even_numbers.append(number)
                                    else:
                                        pass
                                for number in range(number_one, number_two + 1):
                                    if number % 2 != 0:
                                        odd_numbers.append(number)
                                    else:
                                        pass
                                for number in range(1, number_two + 1):
                                    if number * number < number_two:
                                        square_numbers.append(number * number)
                                    else:
                                        pass
                                print("All the even numbers between {0} and {1} are: {2}\n"
                                      "All the odd numbers between {0} and {1} are: {3}\n"
                                      "All the square numbers bwtween {0} and {1} are: {4}".format(number_one, number_two, even_numbers, odd_numbers, square_numbers))
                                number_one = -1
                                menu = input("Number Generator \n(C)hoose numbers: \n(F)inish: \n>>>").upper()
                        except ValueError:
                            print("You must enter a number")
            except ValueError:
                print("You must enter a number")
    else:
        print("Must be a valid input")
        menu = input("Number Generator \n(C)hoose numbers: \n(F)inish: \n>>>").upper()
print("END")