from requests import get
from bs4 import BeautifulSoup


def main():
    res = get(
        "https://medium.com/towards-data-science/the-5-basic-statistics-concepts-data-scientists-need-to-know-2c96740377ae"
    )

    soup = BeautifulSoup(res.content, "html.parser")
    h1s = soup.find_all(name="h1", recursive=True)
    print()

    for h1 in h1s:
        print(h1.getText())


if __name__ == "__main__":
    main()
