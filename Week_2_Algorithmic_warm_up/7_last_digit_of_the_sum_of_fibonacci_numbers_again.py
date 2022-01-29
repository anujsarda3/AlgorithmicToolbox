# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    fib = [0 for i in range(60)]
    last_digit = [0 for i in range(60)]
    fib[1] = 1
    last_digit[1] = 1
    from_index %= 60
    to_index %= 60
    sum = 0
    for i in range(2, 60):
        fib[i] = (fib[i - 1] + fib[i - 2]) % 10

    if from_index <= to_index:
        for i in range(from_index, to_index + 1):
            sum += fib[i]
    else:
        for i in range(from_index, 60):
            sum += fib[i]
        for i in range(0, to_index + 1):
            sum += fib[i]

    return sum%10



if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
