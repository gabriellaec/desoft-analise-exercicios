def soma_impares(lista):
    s=0
    for i in lista:
        if not i%2==0:
            s=i+s
        else:
            None
    return s