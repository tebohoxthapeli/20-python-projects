from qrcode import QRCode, ERROR_CORRECT_L
from re import compile


def generate_qrcode(text: str, qrcode_name: str) -> None:
    qr = QRCode(version=1, error_correction=ERROR_CORRECT_L)
    qr.add_data(text)
    qr.make()

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"{qrcode_name}.png")

    print(f"\n'{qrcode_name}.png' successfully created!")


def prompt_user(message) -> str:
    regex = r"^\s+$"
    pattern = compile(regex)

    while True:
        inp = input(f"\n{message}\n")
        match = pattern.search(inp)

        if match is None and inp:
            return inp

        print(f"Your input is either empty or is just whitespace. Don't do that...")


def main():
    text = prompt_user("Enter some text that you would like to generate a QR code for:")

    qrcode_name = prompt_user(
        "What would you like to call the generated QR code image?:"
    )

    generate_qrcode(text, qrcode_name)


if __name__ == "__main__":
    main()
