def quantos_uns():
    n = str(input("Digite um número qualquer: "))
    i = 0
    qn1 = 0
    while i < len(n):
        if n[i]== str(1):
            qn1 += 1
            i += 1
        else:
            i += 1
    return qn1