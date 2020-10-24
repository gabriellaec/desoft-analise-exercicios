def verifica_numero(n):
    num = str(n)
    numero = int(num)
    i = 0
    valor = 0
    while i < len(num):
        valor += int(num[i])**(int(num[i]))
        i += 1
    if numero == valor:
        return True
    else:
        return False