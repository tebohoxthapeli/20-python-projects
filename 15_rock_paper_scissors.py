from random import choice

play_options = {"r": "rock", "p": "paper", "s": "scissors"}
l, w = "lost", "won"

# from user's perspective:
game_logic = {"r": {"p": l, "s": w}, "p": {"r": w, "s": l}, "s": {"r": l, "p": w}}


def draw_line(rl_char: str = "|", cen_chars: str = " ", inner_chars: str = " ") -> None:
    if cen_chars == "-":
        inner_chars = cen_chars

    print(f"{rl_char}{cen_chars.center(68, inner_chars)}{rl_char}")


def print_scores(user_score: int, computer_score: int, game_num: int) -> None:
    draw_line(rl_char="+", cen_chars="-")

    message = ""

    if user_score > computer_score:
        message = "YOU WON"
    elif computer_score > user_score:
        message = "YOU LOST"
    else:
        message = "IT WAS A TIE"

    draw_line(cen_chars=message)
    draw_line()
    draw_line(cen_chars=f"Computer: {computer_score}/{game_num}")
    draw_line(cen_chars=f"You: {user_score}/{game_num}")
    draw_line(rl_char="+", cen_chars="-")
    print()


def get_user_input() -> str:
    while True:
        user_input = input(
            "\nDo you want to play r (rock), p (paper) or s (scissors)?: (q to quit)\n"
        ).lower()[0]

        if user_input in list(play_options) + ["q"]:
            return user_input

        print("Invalid input entered. Try again.")


def main():
    user_score, computer_score, game_num = 0, 0, 0

    while True:
        user_input = get_user_input()

        if user_input == "q":
            if game_num:
                print_scores(user_score, computer_score, game_num)

            print("\nQuitting program...")
            quit()

        game_num += 1
        computer_input = choice(list(play_options))

        print(f"The computer chose: {play_options[computer_input]}")

        if user_input == computer_input:
            computer_score += 1
            user_score += 1

            print("Tied for this round")
        else:
            result = game_logic[user_input][computer_input]

            if result == "won":
                user_score += 1
            else:
                computer_score += 1

            print(f"You {result} this round.")


if __name__ == "__main__":
    main()
