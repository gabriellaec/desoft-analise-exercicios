def verifica_numero(x):
    i=input("n?: ")
    if i == sum(int(x) ** int(x) for x in str(i)):
        return True
    else:
        return False