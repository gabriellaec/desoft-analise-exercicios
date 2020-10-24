def collatz(n):
    while n != 1:
        if n % 2 == 0:
            k = n / 2
            print(k)
        else:
            y = n * 3 + 1
            print(y)