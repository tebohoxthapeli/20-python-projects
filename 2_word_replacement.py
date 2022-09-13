def replace_word(sen: str, string: str, repl: str) -> str:
    return sen.replace(string, repl)


def main():
    sen = input("\nEnter your sentence:\n")
    string = input("\nWhat do you want to replace?:\n")
    repl = input("\nWhat do you want to replace it with?:\n")

    print(replace_word(sen, string, repl))


if __name__ == "__main__":
    main()
