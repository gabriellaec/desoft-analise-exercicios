def junta_nome_sobrenome(nome, sobrenome):
    
    junta = []
    i = 0
    while i <len(nome):
        junta.append(nome[i]+sobrenome[i])
        i+=1
    return junta