def classifica_lista(lista):
    for i in range(len(lista)-1):
        if len(lista) < 2:
            classificacao = "nenhum"
        elif lista[i+1] > lista[i]:
            classificacao = "crescente"
        elif lista[i+1] < lista[i]:
            classificacao = "decrescente"
        else:
            classificacao = "nenhum"
        print(classificacao)