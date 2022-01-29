# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    output = [float('inf'), 1, 1, 1]
    outputSequence = [n]
    numOperations = 0
    operations = [1, 2, 3]
    for i in range(4, n+1):
        # print(i)
        output.append(float('inf'))
        for op in operations:
            # print(op)
            if op == 3 and i % 3 == 0:
                numOperations = output[i//3] + 1
            elif op == 2 and i % 2 == 0:
                numOperations = output[i//2] + 1
            else:
                numOperations = output[i-1] + 1
            if numOperations < output[i]:
                # print(numOperations, i)
                output[i] = numOperations

    # print(output)

    while n > 1:
        op1 = op2 = op3 = 0
        op1 = n-1
        if n % 2 == 0:
            op2 = int(n/2)
        if n % 3 == 0:
            op3 = int(n/3)

        if output[op3] <= output[op2] and output[op3] <= output[op1]:
            outputSequence.append(op3)
            n = op3
        elif output[op2] < output[op1] and output[op2] < output[op3]:
            outputSequence.append(op2)
            n = op2
        else:
            outputSequence.append(op1)
            n = op1

    # output.append(1)
    # print(outputSequence)
    return outputSequence[::-1]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
