# python3


def edit_distance(first_string, second_string):

    n = len(first_string) + 1
    m = len(second_string) + 1
    D = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        D[i][0] = i
    for i in range(m):
        D[0][i] = i

    for j in range(1, m):
        for i in range(1, n):
            ins = D[i][j-1] + 1
            dele = D[i-1][j] + 1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 1
            if first_string[i-1] == second_string[j-1]:
                D[i][j] = min(ins, dele, match)
            else:
                D[i][j] = min(ins, dele, mismatch)

    return D[n-1][m-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
