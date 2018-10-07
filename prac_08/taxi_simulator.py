from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = Taxi("Basic Taxi", 100), SilverServiceTaxi("Siver Service Taxi", 100, 3)
    menu = input("Select a taxi from the list below to see exact details.\n(B)asic Taxi\n(S)ilver Service Taxi\n(Q)uit\n>>>").upper()
    while menu != "Q":
        if input == "B":
            print("Basic Taxi")
            menu = input("Select a taxi from the list below to see exact details.\n(B)asic Taxi\n(S)ilver Service Taxi\n(Q)uit\n>>>").upper()
        elif input == "S":
            print("Siver Service Taxi")
            menu = input(
                "Select a taxi from the list below to see exact details.\n(B)asic Taxi\n(S)ilver Service Taxi\n(Q)uit\n>>>").upper()
        else:
            print("Invalid input")
            menu = input(
                "Select a taxi from the list below to see exact details.\n(B)asic Taxi\n(S)ilver Service Taxi\n(Q)uit\n>>>").upper()


main()