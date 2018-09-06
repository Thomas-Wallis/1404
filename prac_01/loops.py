def main():
    for i in range(1, 21, 2):
        print(i, end=' ')
        print()
        for i in range(0, 101, 10):
            print(i, end=' ')
        print()
        for i in range(20, 0, -1):
            print(i, end=' ')
        print()
        num_stars = (int(input("Number of stars: ")))
        for i in range(0, num_stars, 1):
            print("*", end=' ')
        print()
        for i in range(1, num_stars + 1, 1):
            print("*" * i)
        print()


main()