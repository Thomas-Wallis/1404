def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = celcius_to_fahreneheit()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = fahreneheit_to_celcius()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celcius_to_fahreneheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def fahreneheit_to_celcius():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

main()