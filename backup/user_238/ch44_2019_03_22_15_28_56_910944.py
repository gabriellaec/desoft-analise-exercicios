def soma(lista):
    i=0
    soma=0
    tamanho=len(lista)
    while i < tamanho:
        soma+=lista[i]
        i+=1
    return soma
lista=[1,2,3,4,5]
print(soma(lista))