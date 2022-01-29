# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3


    pre, post = 0,1
    for i in range(0,m*m):
        pre,post = post, (pre+post)%m
        if(pre==0 and post==1):
            break

    n = n%(i+1)

    a,b=0,1

    if n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range(1,n):
            num = a+b
            a = b
            b = num

    return num%m


if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
