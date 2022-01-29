# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    denominations = [10,5,1]
    coins = 0
    for i in denominations:
        while money/i >=1:
            coins +=1
            money -= i

    return coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
