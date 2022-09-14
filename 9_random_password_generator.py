"""
ascii_letters: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits: '0123456789'
punctuation: '!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'
(note: the backslash above has been escaped. it's actually just one slash)
"""


from string import ascii_letters, digits, punctuation
from random import shuffle, choice


def get_pass_len() -> int:
    while True:
        try:
            inp = input("\nHow long would you like your password to be? (q to quit):\n")

            if inp == "q":
                print("Quiting program...")
                quit()

            inp = float(inp)

            if inp % 1 != 0:
                raise ValueError()

            return int(inp)
        except ValueError:
            print("Error: enter a valid number.")


def gen_password() -> str:
    chars = list(ascii_letters + digits + punctuation)

    # randomise list of chars
    shuffle(chars)

    password = []

    for _ in range(get_pass_len()):
        # choice() chooses a random element from the sequence
        password.append(choice(chars))

    # randomise the password
    shuffle(password)

    return "".join(password)


def main():
    print(f"Generated password: {gen_password()}")


if __name__ == "__main__":
    main()
