# python3

from itertools import permutations


def max_dot_product_naive(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product


def max_dot_product(first_sequence, second_sequence):
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    first_sequence.sort(reverse=True)
    second_sequence.sort(reverse=True)
    final = [first_sequence[i]*second_sequence[i] for i in range(len(first_sequence))]
    return sum(final)
    ######################################################################################

    # n = len(first_sequence)
    # value = 0
    # for i in range(n):
    #     max_price = max(first_sequence)
    #     max_clicks = max(second_sequence)
    #     value += max_price*max_clicks
    #     index_p = first_sequence.index(max_price)
    #     index_c = second_sequence.index(max_clicks)
    #     first_sequence.pop(index_p)
    #     second_sequence.pop(index_c)
    #
    # return value




if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
