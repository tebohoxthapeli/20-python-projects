from os import environ
from re import compile
from requests import get
from string import punctuation
from typing import Any


def get_word_id() -> str:
    punc = punctuation.replace("-", "")
    regex = f"[\\d{punc}]"
    pattern = compile(regex)

    while True:
        word = input("\nEnter a word: (q to quit)\n").lower()
        print()

        if word == "q":
            print("Quitting program...")
            quit()

        match = pattern.search(word)

        if match is None:
            return word

        print("Error: Enter a valid word.")


def validate_headers(headers: dict) -> bool:
    for h in headers.values():
        if not h:
            return False
    return True


def process_synonyms(synonyms: list[dict]) -> str:
    fin_synonyms = []

    for s in synonyms:
        fin_synonyms.append(s["text"])

    return ", ".join(fin_synonyms)


def process_entry(entry: dict[str, list]) -> dict:
    fin_entry = {}

    pronuns = entry.get("pronunciations", [])
    senses = entry.get("senses", [])
    etym = entry.get("etymologies", [])

    if pronuns:
        p: dict[str, str] = pronuns[0]

        phon_spell = p.get("phoneticSpelling", "")
        aud_file = p.get("audioFile", "")

        if phon_spell:
            fin_entry["phonetic spelling"] = phon_spell

        if aud_file:
            fin_entry["audio file"] = aud_file

    if senses:
        s: dict[str, list] = senses[0]

        defin: str = s["definitions"][0]
        fin_entry["definition"] = defin.capitalize()

        egs = s.get("examples", [])
        syns = s.get("synonyms", [])

        if egs:
            eg: str = egs[0]["text"]
            fin_entry["example"] = eg.capitalize()

        if syns:
            fin_entry["synonyms"] = process_synonyms(syns)

    if etym:
        fin_entry["etymology"] = etym[0]

    return fin_entry


def process_lexical_entry(le: dict) -> dict[str, Any]:
    entries: dict[str, list] = le["entries"][0]

    return {"lexical category": le["lexicalCategory"]["id"], **process_entry(entries)}


def draw_line(num_dashes: int) -> None:
    print(f"{'-'.center(num_dashes, '-')}\n\n")


def main():
    domain = "od-api.oxforddictionaries.com"

    headers = {
        "app_id": environ.get("app_id", ""),
        "app_key": environ.get("app_key", ""),
    }

    if not validate_headers(headers):
        print(
            f"\nFatal error: The {domain} API requires app_id and app_key headers for authentication purposes and to function properly. Configure them as environment variables on your system and try again."
        )
        quit()

    # lexical category + definition are always present as long as the api returns results. everything else is sometimes there, sometimes not

    while True:
        word_id = get_word_id()
        url = f"https://{domain}:443/api/v2/entries/en-gb/{word_id}"

        print(f"Hold on...\n\n")
        draw_line(80)

        res: dict = get(url, headers={**headers}).json()
        results = res.get("results", [])

        if results:
            lex_entries: list[dict] = results[0]["lexicalEntries"]

            for idx, le in enumerate(lex_entries, 1):
                p_le = process_lexical_entry(le)

                print(f"{idx}. {p_le['lexical category']}")
                del p_le["lexical category"]

                for heading, val in p_le.items():
                    print(f"\n{heading.upper()}:\n{val}")
                print("\n")
        else:
            print("Info: Word not found.\n\n")

        draw_line(80)


if __name__ == "__main__":
    main()
