def subtracao_de_listas(lista1, lista2):
    i = 0
    n = 0
    run = True
    lista_final = []
    while run:
        if n == len(lista2):
            n = 0
            i+=1
        if lista1[i] != lista2[n]:
            lista_final.append(lista2[n])
            n+=1
        if lista1[i] == lista2[n]:
            n+=1
        if i == len(lista1) and n == len(lista2):
            print(lista_final)
            run = False
        