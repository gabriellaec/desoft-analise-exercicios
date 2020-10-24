def calcula_total_da_nota(lista_preco,lista_quantidade):
    cont=0
    lista_total=[]
    while cont<len(lista_preco) and cont<len(lista_quantidade):
        lista_total.append(lista_preco[cont]*lista_quantidade[cont])
        total+=lista_total
        cont+=1
        
    return 