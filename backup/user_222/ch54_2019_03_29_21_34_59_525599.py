def junta_nome_sobrenome(lista1,lista2):
    i=0
    nome=''
    while i<len(lista1) and len(lista2):
        nome=lista1[i]+lista2[i]
        i+=1
    return nome