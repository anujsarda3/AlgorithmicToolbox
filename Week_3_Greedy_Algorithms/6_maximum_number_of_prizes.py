# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    temp = n
    if n==1:
        summands.append(1)
        return summands

    for i in range(1,n):
        if temp > 2*i:
            summands.append(i)
            temp -= i
        else:
            summands.append(temp)
            return summands



if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
