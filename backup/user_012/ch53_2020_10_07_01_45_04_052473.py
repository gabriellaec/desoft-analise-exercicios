def soma_impares(lista):
    lista_impares=[]
    i=0
    while i < len(lista): #quant. de termos que tem nalista
        if lista[i] % 2 != 0: # checagem se cada termo da lista é ímpar
            lista_impares.append(lista[i]) # tais valores serão adicionados na lista fazia que contem apenas os impares
            i=i+1
        else:
            i=i+1 # se ele não for impar, meu contador vai continuar avançando
    soma = 0
    k=0 
    while k < len(lista_impares):
        soma= soma +lista_impares[k]
        k= k+1
    return soma

    