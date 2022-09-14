import urllib.request as req
from urllib.error import URLError
from re import compile, IGNORECASE


def get_url() -> str:
    regex = r"(https?://)?(www\.)?\w+(?:\.\w+)+"
    pattern = compile(regex, IGNORECASE)

    while True:
        url = input("\nEnter any website's URL:\n")
        match = pattern.search(url)

        if match:
            if not match.group(2):
                url = f"www.{url}"

            if not match.group(1):
                url = f"https://{url}"

            return url

        print(
            "\nInvalid URL format entered. Here's an example of a URL: https://google.com. Try again."
        )


def main():
    url = get_url()

    try:
        res = req.urlopen(url)
        print(f"\n{url} responded with a status code of {res.getcode()}. All looks good.")
    except URLError:
        print(
            f"\nThis site can't be reached. {url}'s DNS address could not be found. Diagnose the problem."
        )


if __name__ == "__main__":
    main()
