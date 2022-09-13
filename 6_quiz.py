def create_final_qnas(l: list[tuple[str, str]]) -> list[dict[str, str]]:
    final_qnas = []

    for i in l:
        q = f"What is the capital city of {i[0]}"
        final_qnas.append({"question": q, "answer": i[1]})

    return final_qnas


def main():
    raw_qnas = [
        ("Namibia", "Windhoek"),
        ("Nigeria", "Abuja"),
        ("Rwanda", "Kigali"),
        ("Senegal", "Dakar"),
        ("Somalia", "Mogadishu"),
        ("Sudan", "Khartoum"),
        ("Eswatini", "Mbabane"),
        ("Tanzania", "Dar es Salaam Dodoma"),
        ("Uganda", "Kampala"),
        ("Zambia", "Lusaka"),
    ]

    score = 0
    qnas = create_final_qnas(raw_qnas)

    for i, qna in enumerate(qnas, 1):
        q, actual_ans = qna.values()
        user_ans = input(f"\n{i}. {q}:\n")

        if user_ans.lower() == actual_ans.lower():
            print("\nCorrect!")
            score += 1
        else:
            print("\nIncorrect")
            print(f"The correct answer is {actual_ans}")

        if i != len(qnas):
            print(f"\nScore so far: {score}/{i}")

    score_perc = (score / len(qnas)) * 100
    emoticon = ":) good!" if score_perc > 50 else ":( apply yourself"
    score_perc = f"{score_perc:.0f}" if score_perc % 1 == 0 else f"{score_perc:.2f}"
    print(f"\nFinal score: {score_perc}% ({score}/{len(qnas)}) {emoticon}")


if __name__ == "__main__":
    main()
