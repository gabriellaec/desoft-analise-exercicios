def junta_nome_sobrenome(lista1,lista2):
    i=0
    while i < len(lista1):
        soma= (lista1[i])+(' ')+(lista2[i])
        a=' '.join(soma)
        i+=1
    print (a)