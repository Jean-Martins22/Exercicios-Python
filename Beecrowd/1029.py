#Fibonacci, Quantas Chamadas?

def fib(num, memo):
    if num in memo:
        return memo[num]
    elif num == 0:
        return (0, 0)
    elif num == 1:
        return (1, 0)
    else:
        val1, calls1 = fib(num - 1, memo)
        val2, calls2 = fib(num - 2, memo)
        memo[num] = (val1 + val2, calls1 + calls2 + 2)
        return memo[num]

def main():
    quant = int(input())
    for _ in range(quant):
        num = int(input())
        memo = {}
        fib_val, calls = fib(num, memo)
        print('fib(%d) = %d calls = %d' % (num, calls, fib_val))

if __name__ == "__main__":
    main()
