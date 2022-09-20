from os import environ
from requests import post
from schedule import run_pending, every
from time import sleep


def send_text():
    phone = environ.get("phone", "")

    res = post(
        "https://textbelt.com/text",
        {
            "phone": phone,
            "message": "Hello world!",
            "key": "textbelt",
        },
    ).json()

    print(res)


def main():
    every().day.at("20:28").do(send_text)

    while True:
        run_pending()
        sleep(1)


if __name__ == "__main__":
    main()
