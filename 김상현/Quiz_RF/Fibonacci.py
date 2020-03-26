def fibonacci(N):
    if N <= 2:
        if N == 0:
            return 0
        else:
            return 1

    return fibonacci(N-1) + fibonacci(N-2)

# 테스트:
print(fibonacci(10))
