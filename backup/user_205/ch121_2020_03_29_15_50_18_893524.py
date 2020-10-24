def subtracao_de_listas (lista1, lista2):
    subtracao = []
    for i in lista1:
        for n in lista2:
            if i != n:
                 subtracao.append(i)
         
    return subtracao