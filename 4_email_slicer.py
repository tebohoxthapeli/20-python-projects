from re import compile


def main():
    r_username = r"(\w+(?:\.\w+)*)"
    r_domain = r"(\w+)"
    r_extension = r"((?:\.\w+)+)"

    regex = f"^{r_username}@{r_domain}{r_extension}$"
    pattern = compile(regex)

    while True:
        email_addr = input(
            "\nEnter an email address or 'exit' to quit the program:\n"
        ).lower()

        if email_addr == "exit":
            quit()

        match = pattern.search(email_addr)

        if not match:
            print("\nThe email address entered does not seem to be valid. Try again.")
        else:
            email_parts = ["username", "mail server", "top-level domain"]
            print("\nHere are the different parts of the entered email address:\n")

            for i, val in enumerate(email_parts, 1):
                print(f"{val}: {match.group(i)}")


if __name__ == "__main__":
    main()
