def is_leap_year(yr: int) -> bool:
    if yr % 100 == 0:
        return yr % 400 == 0
    return yr % 4 == 0


def get_yr():
    while True:
        try:
            yr = input("\nEnter a year: (q to quit)\n")

            if yr.lower() == "q":
                print("Quitting program...")
                quit()
            
            if len(yr) < 4:
                raise ValueError()

            return int(yr)
        except ValueError:
            print("Enter a valid year")


def main():
    while True:
        yr = get_yr()

        if is_leap_year(yr):
            print(f"{yr:0>4d} is a leap year")
        else:
            print(f"{yr:0>4d} is not a leap year")


if __name__ == "__main__":
    main()
