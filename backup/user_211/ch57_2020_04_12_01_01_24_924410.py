def pa(lista):
    n=0
    diferenca = lista[1] - lista[0]
    for i in range(1,len(lista)):
        if (lista[i] - lista[i-1] == diferenca):
            n+=1
    if n==len(lista)-1:
        return True
    else:
        return False
def pg(lista):
    if lista[0]==0:
        return False
    razao = lista[1]/lista[0]
    
    n=0
    for i in range(1,len(lista)):
        if lista[i]/(lista[i-1])==razao: 
            n+=1
    if n==len(lista)-1:
        return True
    else:
        return False

def verifica_progressao(lista):
    if pa(lista)==True and pg(lista)==True:
        return "AG"
    elif pa(lista)==True:
        return "PA"
    elif pg(lista)==True:
        return "PG"
    else:
        return "NA"