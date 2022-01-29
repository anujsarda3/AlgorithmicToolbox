# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    # max_value = [prices[i]/weights[i] for i in range(len(weights))]
    # curr_capacity = capacity
    # value = 0
    # while curr_capacity > 0:
    #     index = max_value.index(max(max_value))
    #     curr_value = max_value[index]
    #     curr_wt = weights[index]
    #     if curr_wt >= curr_capacity:
    #         value += curr_capacity*curr_value
    #         curr_capacity -= curr_wt
    #     else:
    #         value += curr_wt*curr_value
    #         curr_capacity -= curr_wt
    #         max_value.pop(index)
    #         weights.pop(index)
    #
    # return value
    #####################################################################################

    max_value = [(prices[i]/weights[i],weights[i]) for i in range(len(weights))]
    max_value.sort(reverse=True)
    curr_capacity = capacity
    value = 0
    for i in max_value:
        if i[1]>= curr_capacity:
            value += curr_capacity*i[0]
            break
        else:
            value += i[1]*i[0]
            curr_capacity -= i[1]

    return value







if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
