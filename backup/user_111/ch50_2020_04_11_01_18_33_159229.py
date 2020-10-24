def junta_nome_sobrenome(nome,sobrenome):
    nome_completo=[]
    num=len(nome)
    for i in range(num):
        nome_completo.append(nome[ i ]+sobrenome[ i ])
    return nome_completo