def junta_nome_sobrenome(nome,sobrenome):
    nome_completo=[]
    i=0
    num=len(nome)
    while i<num:
        nome_completo.append(nome[i]+sobrenome[i])
        i+=1
    return nome + sobrenome