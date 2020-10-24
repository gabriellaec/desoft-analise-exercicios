def junta_nome_sobrenome(n,s):
    i=0
    soma=[]
    while i<len(n):
        soma.append(n[i] + " " + s[i])
        i+=1
    return soma