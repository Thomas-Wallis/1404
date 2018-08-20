def main():
    score = float(input("Enter score: "))
    grade = determine_grade(score)
    print(grade)


def determine_grade(score):
    if score < 0 or score > 100:
        grade = ("Invalid score")
    elif score >= 90:
        grade = ("Excellent")
    elif score >= 50 and score < 90:
        grade = ("Passable")
    else:
        grade = ("Bad")
    return grade


main()