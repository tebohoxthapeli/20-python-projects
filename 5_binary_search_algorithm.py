def bin_search(target, l: list) -> int:
    iter = 0
    min = 0
    max = len(l) - 1

    while min <= max:
        iter += 1
        print(f"iteration: {iter} -> {l[min:max+1]}")

        mid = (min + max) // 2
        current = l[mid]

        if current == target:
            return mid

        if current < target:
            min = mid + 1
        else:
            max = mid - 1

    return -1


def main():
    item_list = [1, 2, 3, 4, 5, 6]
    target = 2

    found_pos = bin_search(target, item_list)

    if found_pos < 0:
        print("\nNot found.")
    else:
        print(f"\nFound at position: {found_pos}")


if __name__ == "__main__":
    main()
