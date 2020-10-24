def junta_nome_sobrenome(nome, sobrenome):
    lista_nome_sobrenome = []
    i = 0 
    while i < len(nome):
        novo_nome = nome[i] + ' ' + sobrenome[i]
        lista_nome_sobrenome.append(novo_nome)
        i+=1
    
    return lista_nome_sobrenome