
def junta_nome_sobrenome(nome,sobrenome):
    listaa = []
    i = 0
    while i < len(nome) and i < len(sobrenome):
        listaa.append(nome[i] + ' ' + sobrenome[i])
        i+=1
    return listaa