def imprime_tipo(n):
    if n % 3 == 0:
        if n % 5 == 0:
            print("Tipo C")
        else:
            print("Tipo A")
    else:
        if n % 5 == 0:
            print("Tipo B")
        else:
            print("Tipo D")
        
    