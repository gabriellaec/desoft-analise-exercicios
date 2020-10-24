def junta_nome_sobrenome(nome, sobrenome):
    nome_sobrenome = []
    i=0
    for i in range (len(nome)):
        nome_sobrenome.append(nome[i]+sobrenome[i])
        i+=1
    return nome_sobrenome