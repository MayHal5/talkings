from people.person import Person
from validator import validate_age


def main():
    age = 12
    name = "dan"
    validate_age(age)
    dan = Person(name, age)


if __name__ == '__main__':
    main()
