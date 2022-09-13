"""
1. go to gmail account and setup 2 factor authentication.
2. generate app password.
3. create function to send email.
"""


from email.message import EmailMessage
from ssl import create_default_context
from smtplib import SMTP_SSL


def main():
    mail = EmailMessage()

    from_addr = input("\nEnter your email address:\n")
    password = input("\nEnter its password:\n")

    # this is a temp email address generated using temp-mail.org
    to_addr = "hipomi7114@laluxy.com"

    mail["From"] = from_addr
    mail["To"] = to_addr
    mail["Subject"] = "Happiness evaluation"

    body = """
    How happy are you? Want to take a quick test to find out? No? Okay. Maybe next time.
    """

    mail.set_content(body)

    with SMTP_SSL(
        host="smtp.gmail.com", port=465, context=create_default_context()
    ) as smtp:
        smtp.login(from_addr, password)
        smtp.sendmail(from_addr, to_addr, msg=mail.as_string())
        print(f"\nEmail sent to {to_addr} successfully!")


if __name__ == "__main__":
    main()
