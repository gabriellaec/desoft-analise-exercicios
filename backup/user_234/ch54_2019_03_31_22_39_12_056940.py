def junta_nome_sobrenome(lista1, lista2):
    lista_nome_inteiro=[]
    i=0
    while i < len(lista1) and len(lista2):
        nome_inteiro = lista1[i] + ' ' + lista2[i]
        lista_nome_inteiro.append(nome_inteiro)
        i+=1
    return lista_nome_inteiro