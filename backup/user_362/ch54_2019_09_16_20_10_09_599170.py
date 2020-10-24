def junta_nome_sobrenome(nome,sobrenome):
    
    nome_sobre=[]
    i=0
    while i <len(nome):
        n=nome[i]+sobrenome[i]
        nome_sobre.append(n)
        i+=1
    return nome_sobre
    