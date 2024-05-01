T = int(input())
for _ in range(T):
    n = int(input())

    fib = [0, 1] + [0]*(n-1)
    calls = [0]*(n+1)

    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
        calls[i] = calls[i-1] + calls[i-2] + 2

    print("fib({}) = {} calls = {}".format(n, calls[n], fib[n]))
