# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7

    # a = 0
    # b = 1
    # num = 1
    # if n == 0:
    #     return a
    # elif n == 1:
    #     return b
    # else:
    #     for i in range(1, n):
    #         num = a + b
    #         a = b
    #         b = num%10
    #
    # return num%10
    #######################################################################

    fib = [0 for i in range(60)]
    fib[1] = 1
    n = n % 60
    for i in range(2, n + 1):
        fib[i] = (fib[i - 1] + fib[i - 2]) % 10

    return fib[n]%10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number_naive(input_n))
