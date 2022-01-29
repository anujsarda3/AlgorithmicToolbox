# python3
# def output_alignment(mat, i, j, seq):
#     final_seq = []
#     # print(i, j)
#     while i > 0 and j > 0:
#         print(i, j)
#         if mat[i][j] == mat[i-1][j]:
#             i -= 1
#         elif mat[i][j] == mat[i][j-1]:
#             j -= 1
#         else:
#             i -= 1
#             j -= 1
#             print(seq[i])
#             final_seq.append(seq[i])
#
#     return final_seq


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    len_seq1 = len(first_sequence) + 1
    len_seq2 = len(second_sequence) + 1

    D = [[0 for i in range(len_seq2)] for j in range(len_seq1)]

    for i in range(1, len_seq1):
        for j in range(1, len_seq2):
            if first_sequence[i-1] == second_sequence[j-1]:
                D[i][j] = D[i-1][j-1] + 1
            else:
                D[i][j] = max(D[i-1][j], D[i][j-1])

    for i in D:
        for j in i:
            print(j, end = " ")
        print()

    # seq = output_alignment(D, len_seq1-1, len_seq2-1, first_sequence)
    # print(seq)
    return D[len_seq1-1][len_seq2-1]



if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
