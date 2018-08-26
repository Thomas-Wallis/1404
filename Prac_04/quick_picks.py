import random
min_picks = 1
max_picks = 45
numbers_per_line = 6
number_of_quick_picks = int(input("How many quick picks? "))
while number_of_quick_picks < 1:
    print("Please select a number greater than 1")
    number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_pick = []
    for x in range(numbers_per_line):
        number = random.randint(min_picks, max_picks)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join("{:2}".format(number) for number in quick_pick))