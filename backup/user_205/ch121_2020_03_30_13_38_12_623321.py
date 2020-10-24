def subtracao_de_listas (lista1, lista2):
    subtracao = []
    for i in lista1:
            if not i in lista2:
                 subtracao.append(i)
         
    return subtracao