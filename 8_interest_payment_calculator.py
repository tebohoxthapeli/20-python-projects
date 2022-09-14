from re import compile, IGNORECASE


def get_user_input(message: str) -> float:
    while True:
        try:
            inp = input(f"\n{message}\n")
            inp = inp.replace(" ", "")

            return float(inp)

        except ValueError:
            print("Invalid input entered. Try again.")


def get_tenure() -> int:
    regex = r"^(\d+)y (\d{,2})m$"
    pattern = compile(regex, IGNORECASE)

    while True:
        tenure = input(
            "\nEnter the agreed upon duration to pay off the loan (in the format: <x>y <y>m, eg. 1y 6m):\n"
        )

        match = pattern.search(tenure)

        if match:
            yrs = match.group(1)
            mons = match.group(2)

            return int(yrs) * 12 + int(mons)

        print("Invalid input entered. Try again")


def main():
    P = get_user_input("Enter loan amount:")
    ann_int_rate = get_user_input("Enter annual interest rate:")
    n = get_tenure()

    # rate of interest is calculated monthly:
    r = ann_int_rate / 12 / 100

    emi = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    print(f"\nMonthly payment: {emi:,.2f}")


if __name__ == "__main__":
    main()
