from PIL import Image


def resize_image(size: tuple[int, int]) -> None:
    img_name = "8e0a7654-ba2f-4340-a0dd-8f60c2cacba8.jpg"
    img = Image.open(img_name)
    w, h = size
    resized_img = img.resize(size)
    resized_img.save(f"resized_{w}_x_{h}_{img_name}")

    print("\nImage resized.\n")
    print(f"old size: {img.size}")
    print(f"new size: {size}")


def get_size_param(_type: str) -> int:
    while True:
        try:
            return int(input(f"Enter a {_type}: "))
        except ValueError:
            print(f"Invalid {_type} entered. Try again.\n")


def main():
    print()
    w = get_size_param("width")
    h = get_size_param("height")

    resize_image((w, h))


if __name__ == "__main__":
    main()
