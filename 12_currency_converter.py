# exchange rate as at 14.09.2022
USD_TO_GBP = 0.87


def convert_to_pounds(dollars: float) -> float:
    return dollars * USD_TO_GBP


def main():
    while True:
        try:
            dollars = input("\nEnter amount in dollars: (q to quit)\n")

            if dollars.lower() == "q":
                print("Quitting program...")
                quit()

            dollars = float(dollars)
            pounds = convert_to_pounds(dollars)
            print(f"{dollars:,.2f} USD -> {pounds:,.2f} GBP")
        except ValueError:
            print("Enter a valid amount.")


if __name__ == "__main__":
    main()
