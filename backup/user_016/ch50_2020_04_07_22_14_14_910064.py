def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    lista = len(nome)
    while i < len(nome):
        lista[i] = nome[i] , sobrenome[i]
        i +=1
    print(lista)