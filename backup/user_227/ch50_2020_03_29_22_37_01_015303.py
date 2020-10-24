def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    lista =[]
    while i < len(nome):
        completo = nome[i] + " " + sobrenome[1]
        lista.append(completo)
        
    return lista
