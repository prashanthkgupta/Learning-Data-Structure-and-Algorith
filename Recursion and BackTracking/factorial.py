def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def factorial_iterative(n):
    stack = []
    fact = 1
    for i in range(n, -1, -1):
        if i == 0:
            while len(stack) > 0:
                fact *= stack.pop()
            break
        stack.append(i)

    return fact


if __name__ == "__main__":
    print(factorial_iterative(3))
