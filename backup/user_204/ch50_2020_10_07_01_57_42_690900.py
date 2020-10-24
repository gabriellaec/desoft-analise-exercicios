nova = []
def junta_nome_sobrenome(lista1,lista2):
    i = 0
    while i < len(lista1):
        nova.append(lista1[i] + " " + lista2[i])
        i += 1
    return nova