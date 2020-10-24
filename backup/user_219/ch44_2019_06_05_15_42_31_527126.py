def soma_valores(lista):
    contador=0
    soma=0
    tamanholista=len(lista)
    while contador<tamanholista:
        soma+=soma+lista[contador]
        contador+=1
    return soma
        