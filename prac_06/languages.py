"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language client code.
"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983)
    java = ProgrammingLanguage("Java", "Static", True, 1995)

    languages = [ruby, visual_basic, python, c_plus_plus, java]
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()