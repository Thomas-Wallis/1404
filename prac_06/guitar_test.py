from prac_06.guitar import Guitar
import datetime

CURRENT_YEAR = datetime.date.today().year


def run_tests():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40
    guitar = Guitar(name, year, cost)
    another = Guitar("Another Guitar", 2012, 1512.9)
    print("{} get_age() - Expected {}. Got {}".format(guitar.name, CURRENT_YEAR - year,
                                                      guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another.name, CURRENT_YEAR - another.year,
                                                      another.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,
                                                         True,
                                                         guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another.name,
                                                         False,
                                                         another.is_vintage()))
if __name__ == '__main__':
    run_tests()