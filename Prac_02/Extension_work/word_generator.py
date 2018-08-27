import random
VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
INVALID_CHAR = "aeioubdfghjklmnpqrstwxyz!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    word_format = input(str("Example format - ccvcvvc\nMust contain only c - consonants and v - vowels"
                            "\nEnter the format you would like your word to use: ")).lower()
    while not check_format(word_format):
        print("You may only enter c - consonants and/or v - vowels")
        word_format = input(str("Example format - ccvcvvc\nMust contain only c - consonants and v - vowels"
                                "\nEnter the format you would like your word to use: ")).lower()
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    print(word)


def check_format(word_format):
    count = 0
    for char in word_format:
        if char in INVALID_CHAR:
            count += 1
        elif char.isdigit():
            count += 1
        else:
            pass
    if count > 0:
        return False
    else:
        return True


main()
