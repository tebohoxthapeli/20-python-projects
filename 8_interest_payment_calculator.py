def get_user_input(message: str, val_type: str) -> float | int:
    while True:
        try:
            inp = input(f"\n{message}\n")
            inp = inp.replace(" ", "")

            if val_type == "float":
                return float(inp)
            elif val_type == "int":
                return int(inp)

        except ValueError:
            print("Invalid input entered. Try again.")


def main():
    P = get_user_input("Enter loan amount:", "float")
    ann_int_rate = get_user_input("Enter annual interest rate:", "float")
    num_yrs = get_user_input("Enter number of years to pay loan off:", "int")

    # rate of interest is calculated monthly:
    r = ann_int_rate / 12 / 100

    # calc months from years:
    n = num_yrs * 12

    emi = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    print(f"\nMonthly payment: {emi:.2f}")


if __name__ == "__main__":
    main()
