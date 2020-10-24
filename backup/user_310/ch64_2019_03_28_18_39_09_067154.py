def nome_usuario(nome):
    usuario=0
    
    i=0
    n=-1
    
    while i<len(nome):
        if nome[n]=="@":
            usuario=nome[0:n]
        i+=1
        n-=1
    return usuario