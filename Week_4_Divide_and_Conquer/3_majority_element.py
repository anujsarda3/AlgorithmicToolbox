# python3


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def merge_sort(elem):
    n = len(elem)
    if n == 1:
        return elem

    mid = n // 2
    # print(elem)
    b = merge_sort(elem[:mid])
    c = merge_sort(elem[mid:])
    # print("b:", b)
    # print("c:", c)

    a = merge(b, c)

    return a


def merge(a1, a2):
    len1 = len(a1)
    len2 = len(a2)
    i, j = 0, 0
    final = []
    # print(a1)
    # print(a2)
    while i < len1 and j < len2:
        if a1[i] > a2[j]:
            # print("A1")
            final.append(a2[j])
            # a2.remove(a2[j])
            j += 1
        else:
            # print("A2")
            final.append(a1[i])
            # a1.remove(a1[i])
            # print(a1)
            i += 1
    # print(i,j)
    while i < len1:
        final.append(a1[i])
        i += 1
    while j < len2:
        final.append(a2[j])
        j += 1

    return final

def majority_element(elements):
    assert len(elements) <= 10 ** 5
    ################################################################
    # n = len(elements)
    # if n==2:
    #     if elements[0]==elements[1]:
    #         return 1
    #     else:
    #         return 0
    #
    # m = n//2
    # B = majority_element(elements[:m-1])
    # C = majority_element(elements[m:])
    #
    # if B==1 or C==1:
    #     return 1
    # else:
    #     return 0
    ################################################################
    n = len(elements)
    count = 0
    arr = merge_sort(elements)
    mid_idx = n//2
    mid = arr[mid_idx]
    for i in range(n):
        if arr[i]== mid:
            count += 1

    if count > mid_idx:
        return 1
    return 0

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
