def junta_nome_sobrenome(n, s):
    nome_sobrenome=[]
    
    i=0
    
    while i<len(n):
        nome="{0} {1}".format(n[i], s[i])
        nome_sobrenome.append(nome)
        i+=1
    return nome_sobrenome