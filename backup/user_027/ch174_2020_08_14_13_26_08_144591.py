def imprime_tipo(n: int):
    if (n % 5 != 0) and (n % 3 == 0):
        print("Tipo A")
    elif (n % 5 == 0) and (n % 3 != 0):
        print("Tipo B")
    elif (n % 15 == 0):
        print("Tipo C")
    else:
        print("Tipo D")