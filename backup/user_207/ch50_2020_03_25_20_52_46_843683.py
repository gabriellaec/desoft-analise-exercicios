nome =[]
sobrenome =[]
nome_sobrenome =[]
def junta_nome_sobrenome(nome, sobrenome):
    i=0
    while i<len(nome):
        nome_sobrenome.append(nome[i] + ' ' + sobrenome[i])
        i += 1