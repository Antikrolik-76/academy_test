def division(a: int|float, b: int|float):
    if b == 0:
        raise ZeroDivisionError("Деление на 0 невозможно")
    return a/b


def main():
    for i, j in enumerate([1, 2, 3], 0):
        try:
            d = division(j, i)
        except ZeroDivisionError as e:
            print(e)
        else:
            print(d)


if __name__ == "__main__":
    main()
