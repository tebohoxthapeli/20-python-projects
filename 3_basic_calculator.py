Number = int | float


def add(a: Number, b: Number) -> None:
    print(f"{a} + {b} = {a+b}")


def subtr(a: Number, b: Number) -> None:
    print(f"{a} - {b} = {a-b}")


def multi(a: Number, b: Number) -> None:
    print(f"{a} * {b} = {a*b}")


def div(a: Number, b: Number) -> None:
    ans = a / b

    if not a % b:
        ans = int(ans)

    print(f"{a} / {b} = {ans}")


def get_calc_mode() -> str:
    while True:
        mode = input(
            "\nWhat do you want to do?:\n\na) Addition\nb) Subtraction\nc) Multiplication\nd) Division\n\n"
        )

        if mode.lower() in ["a", "b", "c", "d"]:
            return mode

        print(
            "Invalid input entered. Only a, b, c, and d are accepted values. Try again.\n"
        )


def get_operands() -> list[int]:
    numbers = []

    for i in range(1, 3):
        while True:
            try:
                number = float(input(f"\nEnter number {i}:\n"))

                if number % 1 == 0:
                    number = int(number)

                numbers.append(number)
                break
            except:
                print("\nEnter a valid numerical digit.")

    return numbers


def main():
    while True:
        mode = get_calc_mode()
        op = get_operands()

        match mode:
            case "a":
                add(*op)
            case "b":
                subtr(*op)
            case "c":
                multi(*op)
            case _:
                div(*op)

        is_exit = input(
            "\nEnter any key to perform another calculation or 'exit' to exit the program.\n"
        )

        if is_exit.lower() == "exit":
            print("\nHate to see you go!")
            quit()


if __name__ == "__main__":
    main()
