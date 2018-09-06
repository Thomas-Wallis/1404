MIN_LENGTH = 6


def main():
    print("Please enter a valid password.")
    print("your password must contain at least 6 characters.")
    password = get_password()
    hide_password_display(password)


def get_password():
    password = input("> ")
    while not valid_password(password):
        print("Invalid password.")
        password = input("> ")
    return password


def valid_password(password):
    if len(password) < MIN_LENGTH:
        return False
    else:
        return True


def hide_password_display(password):
    for i in range(0, len(password)):
        print("*", end='')


main()