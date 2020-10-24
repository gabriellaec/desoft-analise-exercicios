def primos_entre(a, b):
    soma = 0
    for n in range(a+1, b, -2):
        if p % n != 0:
            if p >= a and p <= b:
                soma += 1
    return soma