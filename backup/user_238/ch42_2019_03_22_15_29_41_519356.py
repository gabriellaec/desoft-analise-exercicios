def encontra1(numero):
    i=0
    soma=0
    tamanho=len(numero)
    while i < tamanho:
        if numero[i] == '1':
            soma+=1
        i+=1
    return soma
numero=10001111
print(encontra1(numero))