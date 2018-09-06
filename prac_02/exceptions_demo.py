"""
Answer the following questions:
1. When will a ValueError occur?
- When any input other than a number is entered
2. When will a ZeroDivisionError occur?
- When the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""


def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")


main()