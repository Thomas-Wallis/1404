from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


MENU = "(Q)uit, (C)hoose taxi, (D)rive"
def main():
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxis available: ")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                while taxi_choice > len(taxis) or taxi_choice < 1:
                    print("Taxi is not listed. Please choose from available taxis.")
                    print("Taxis available: ")
                    display_taxis(taxis)
                    taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice - 1]
                print("Bill to date: ${}".format(total_bill))
                print(MENU)
                menu_choice = input(">>> ").upper()
            except ValueError:
                print("Invalid input. Please choose from available taxis.")
        elif menu_choice == "D" and current_taxi != None:
            current_taxi.start_fare()
            drive_distance = float(input("Drive how far? "))
            current_taxi.drive(drive_distance)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you {}".format(current_taxi.name, trip_cost))
            total_bill += trip_cost
            print("Bill to date: ${}".format(total_bill))
            print(MENU)
            menu_choice = input(">>> ").upper()
        elif menu_choice == "D" and current_taxi == None:
            print("You can't drive without first having selected a taxi.")
            print(MENU)
            menu_choice = input(">>> ").upper()
        else:
            print("Invalid input.")
            print(MENU)
            menu_choice = input(">>> ").upper()
    print("Total trip cost ${}".format(total_bill))
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    """Display numbered list of taxis."""
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i+1, str(taxi)))


main()
