# python3


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    len_seq1 = len(first_sequence)+1
    len_seq2 = len(second_sequence)+1
    len_seq3 = len(third_sequence)+1

    D = [[[0 for i in range(len_seq3)] for j in range(len_seq2)] for k in range(len_seq1)]

    for i in range(1, len_seq1):
        for j in range(1, len_seq2):
            for k in range(1, len_seq3):
                if first_sequence[i-1] == second_sequence[j-1] == third_sequence[k-1]:
                    D[i][j][k] = D[i-1][j-1][k-1] + 1
                else:
                    D[i][j][k] = max(D[i-1][j][k], D[i][j-1][k], D[i][j][k-1])

    return D[len_seq1-1][len_seq2-1][len_seq3-1]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
