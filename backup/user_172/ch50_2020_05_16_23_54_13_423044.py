def junta_nome_sobrenome(lista_n, lista_s):
    lista = []
    i = 0
    while i < len(lista_n):
        a = '{0} {1}'.format (lista_n[i], lista_s[i])
        lista.append(a)
        i+=1
        
    print (lista)
    return lista
        