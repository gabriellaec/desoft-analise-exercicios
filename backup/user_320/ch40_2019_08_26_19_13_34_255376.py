def fatorial(numero):
    fat = 1
    while numero > 0:
        fat *= numero
        numero -= 1
    return fat

print(fatorial(5))