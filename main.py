def division(a: int|float, b: int|float):
    return a/b


def main():
    for i, j in enumerate([1, 2, 3], 0):
        d = division(j, i)

        print(d)



if __name__ == "__main__":
    main()
