import math
x = input("manda o numero!")
x = int(x)


def f(x):
    return (-1) ** x


print(f(x))


k = int(input("vamos multiplicar por quanto?"))

def formatTest(p):
    print("pi multiplicado por {0} eh {1: .8f}".format(p, math.pi * p))


print(formatTest(k))