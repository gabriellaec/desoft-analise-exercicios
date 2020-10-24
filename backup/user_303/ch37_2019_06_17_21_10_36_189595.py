def verifica_primo(k): 
    c=2
    p=True
    while c<k:
        if k%c==0: 
            p=False 
        c+=1
    return p    

def lista_primos(n): 
    c=2
    lista_p=[]
    while len(lista_p)<c:
        if verifica_primo(c):
            lista_p.append(c)
        c+=1
    return lista_p