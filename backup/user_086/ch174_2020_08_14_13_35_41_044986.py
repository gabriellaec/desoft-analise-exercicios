def imprime_tipo(n):
    n = int(n)
    x3 = int(0)
    x5 = int(0)

    div3 = int(3)
    div5 = int(5)

    if n%3 == 0:
        x3=3
    if n%5 == 0:
        x5=5
    
    soma = x3 + x5
    if soma == 3:
        print("Tipo A")
    if soma == 5:
        print("Tipo B")
    if soma == 8:
        print("Tipo C")
    if soma == 0:
        print("Tipo D")