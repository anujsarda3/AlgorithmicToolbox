# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):

    temp = numbers
    list = []
    while numbers != []:
        max_d = 0
        for str1 in numbers:
            if int(str(str1) + str(max_d)) >= int(str(max_d) + str(str1)):
                max_d = str1
        list.append(max_d)
        numbers.remove(max_d)

    return ''.join([str(i) for i in list])


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
