# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)


    len_weights = len(weights)+1

    value_mat = [[0 for i in range(capacity+1)] for j in range(len_weights)]
    # weights.sort()
    for w in range(1, len_weights):
        value = 0
        for i in range(1, capacity+1):
            value_mat[w][i] = value_mat[w-1][i]
            if weights[w-1] <= i:
                # print(w, i)
                value = value_mat[w-1][i-weights[w-1]] + weights[w-1]
                if value > value_mat[w][i]:
                    value_mat[w][i] = value
    # print(weights)
    # print(value_mat)
    return value_mat[len_weights-1][capacity]




if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    # input_capacity = int(input())
    # n = int(input())
    # input_weights = list(map(int, input().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
