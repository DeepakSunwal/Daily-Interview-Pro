def find_missing_ints(numbers):
    return [x for x in range(1, len(numbers)) if x not in numbers]


def main():
    assert find_missing_ints([1, 2, 4, 6, 7, 6, 2]) == [3, 5]


if __name__ == '__main__':
    main()
