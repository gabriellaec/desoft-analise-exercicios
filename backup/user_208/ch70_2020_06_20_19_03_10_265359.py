def esconde_senha (senha):
    i = 0
    tamanho = len(senha)
    while i < tamanho:
        x = senha.replace(senha[i],'*')
        i+=1
        return x    
        