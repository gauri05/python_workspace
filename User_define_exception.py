class AgeInvalid(Exception):
    def __init__(self, value):
        self.value = value


def main():
    try:
        age = int(input("Enter Age"))
        if (age < 18):
            raise (AgeInvalid("Age is invalid"))
    except AgeInvalid as error:
        print("A new exception occured:", error.value)


if __name__ == "__main__":
    main()
