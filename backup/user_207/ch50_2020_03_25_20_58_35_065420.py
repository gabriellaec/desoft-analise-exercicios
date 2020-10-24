def junta_nome_sobrenome(nome, sobrenome):
    i=0
    while i<len(nome) and len(sobrenome):
        nome_sobrenome.append(nome[i] + ' ' + sobrenome[i])
        i += 1
    return nome_sobrenome

print (junta_nome_sobrenome(nome,sobrenome))