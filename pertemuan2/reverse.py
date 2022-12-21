def reverse(*input):
    i = len(input)
    result = []

    while i >= 1:
        result.append(input[i-1])
        i = i - 1

        print(result)

    reverse(1, 2, 4, 7, 2)
