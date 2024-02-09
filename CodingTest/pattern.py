def print_rows(num, i):
    if num == 0:
        return
    if i % 2 == 0:
        print("0", end=" ")
    else:
        print("1", end=" ")

    print_rows(num - 1, i + 1)


def pattern_print(n, i):
    if n == 0:
        return
    print_rows(i, 1)
    print("\n", end="")

    pattern_print(n - 1, i + 1)


if __name__ == '__main__':
    try:
        n = int(input("Enter a positive number: "))
        if n < 0:
            n = int(input("Please enter a positive number: "))

        pattern_print(n, 1)
    except Exception as e:
        print(e)
