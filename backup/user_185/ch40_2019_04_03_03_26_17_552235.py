def fatorial(n):
    index = 1
    multiplicação = index
    while index <= n:
        multiplicação = multiplicação*index
        print(multiplicação)
        index = index + 1
print(fatorial(5))