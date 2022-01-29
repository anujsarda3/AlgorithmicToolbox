# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):


    denomination = [1, 3, 4]
    numCoins = 0
    minNumCoins = [0]
    for i in range(1, money+1):
        minNumCoins.append(float('inf'))
        for denom in denomination:
            if denom <= i:
                numCoins = minNumCoins[i-denom]+1
                if numCoins < minNumCoins[i]:
                    minNumCoins[i] = numCoins

    return minNumCoins[money]



if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
    # print(change_naive(amount))
