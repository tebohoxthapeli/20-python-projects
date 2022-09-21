import matplotlib.pyplot as plt


def draw_two_lines():
    x1 = [2, 4, 5]
    y1 = [2, 3, 6]

    plt.plot(x1, y1, label="Line 1")

    x2 = [1, 2, 3, 4]
    y2 = [1, 2, 3, 5]

    plt.plot(x2, y2, label="Line 2")

    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Demo Graph - Two Lines")
    plt.legend()
    plt.show()


def customisation():
    x = [2, 4, 5]
    y = [2, 3, 6]

    plt.plot(
        x,
        y,
        color="green",
        linestyle="dashed",
        linewidth=3,
        marker="*",
        markerfacecolor="blue",
        markersize=12,
    )

    plt.ylim(1, 8)
    plt.xlim(1, 8)

    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Demo Graph - Customisation")
    plt.legend()
    plt.show()


def main():
    left = [1, 2, 3, 4, 5]
    height = [10, 11, 23, 36, 4]

    tick_label = ["one", "two", "three", "four", "five"]

    plt.bar(left, height, tick_label=tick_label, width=0.8, color=["blue", "orange"])

    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Demo Graph - Bar Chart")
    plt.show()


if __name__ == "__main__":
    main()
