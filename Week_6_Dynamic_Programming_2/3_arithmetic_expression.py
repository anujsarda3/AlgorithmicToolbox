# python3
import operator

def minAndMax(i, j, maxiM, miniM, oper):
    mini = float('inf')
    maxi = float('-inf')
    ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    for k in range(i, j):
        # print("In func:", k)
        a = ops[oper[k]](maxiM[i][k], maxiM[k+1][j])
        b = ops[oper[k]](maxiM[i][k], miniM[k+1][j])
        c = ops[oper[k]](miniM[i][k], maxiM[k+1][j])
        d = ops[oper[k]](miniM[i][k], miniM[k+1][j])
        mini = min(mini, a, b, c, d)
        maxi = max(maxi, a, b, c, d)
    return mini, maxi


def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    numbers = []
    operations = []
    for idx, val in enumerate(dataset):
        if idx % 2 == 0:
            numbers.append(val)
        else:
            operations.append(val)
    lenNumbers = len(numbers)


    minMat = [[0 for i in range(lenNumbers)] for j in range(lenNumbers)]
    maxMat = [[0 for i in range(lenNumbers)] for j in range(lenNumbers)]

    for i in range(lenNumbers):
        minMat[i][i], maxMat[i][i] = int(numbers[i]), int(numbers[i])

    # print(minMat)
    # print(maxMat)
    for op in range(1, lenNumbers):
        for i in range(lenNumbers - op):
            j = i + op
            # print("In Main:", i, j)
            minMat[i][j], maxMat[i][j] = minAndMax(i, j, maxMat, minMat, operations)
    # print(minMat)
    # print(maxMat)

    return maxMat[0][lenNumbers-1]


if __name__ == "__main__":
    print(find_maximum_value(input()))
