from random import randint


def prompt_user():
    while True:
        inp = input("\nWould you like to roll again?: (y for yes or q to quit)\n")

        if inp.lower() == "q":
            print("Quitting program...")
            quit()
        elif inp.lower() != "y":
            print("Invalid input entered. Try again.")
        else:
            break


def roll_dice():
    while True:
        print(f"\nYou rolled a {randint(1, 6)} and a {randint(1, 6)}")
        prompt_user()


def main():
    roll_dice()


if __name__ == "__main__":
    main()
