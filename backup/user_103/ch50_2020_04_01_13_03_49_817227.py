def junta_nome_sobrenome(lista1,lista2):
    i=0
    for lista1[i] in lista2[i]:
        soma= str(lista1)+str(lista2)
        a=' '.join(soma)
        i+=1
    print (a)