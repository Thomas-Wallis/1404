from prac_08.unreliable_car import UnreliableCar


def main():
    my_reliable_car = UnreliableCar("Car 1", 100, 100)
    my_unreliable_car = UnreliableCar("Car 2", 100, 50)
    my_broken_car = UnreliableCar("Car 3", 100, 25)
    scrap_metal = UnreliableCar("Car 4", 100, 0)
    my_reliable_car.drive(50)
    my_unreliable_car.drive(50)
    my_broken_car.drive(50)
    scrap_metal.drive(50)
    print(my_reliable_car)
    print(my_unreliable_car)
    print(my_broken_car)
    print(scrap_metal)


main()