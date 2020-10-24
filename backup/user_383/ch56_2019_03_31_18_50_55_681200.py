def calcula_total_da_nota(lista_preco,lista_quantidade):
    lista_total=[]
    cont=0
    contador=1
    soma=0
    while cont<len(lista_preco) and cont<len(lista_quantidade):
        lista_total.append(lista_preco[cont])
        if lista_quantidade in lista_total:
            contador+=1
        lista_total[cont]=lista_quantidade[cont]*lista_preco[cont]
        soma+=lista_total[cont]
        cont+=1

    return soma