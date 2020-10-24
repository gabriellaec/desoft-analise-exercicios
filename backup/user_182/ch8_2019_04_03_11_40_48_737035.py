def verifica_pa(lista):
    if len(lista)==1:
        return False
    i=1
    r = lista[i]-lista[i-1]
    while i<len(lista):
        if lista[i]-lista[i-1]!=r:
            return False
        i+=1
    return True 

def verifica_pg(lista):
    if len(lista) == 1:
        return False
    t=1
    q=lista[t]/lista[t-1]
    while t< len(lista):
        if lista[t]/lista[t-1]!=q:
            return False
        t+=1
    return True
    
def verifica_progressao(lista):
    if verifica_pa(lista) == True and verifica_pg(lista) == True:
        resultado = "AG"
    if verifica_pa(lista) == True and verifica_pg(lista) == False:
        resultado = "PA"
    if verifica_pa(lista) == False and verifica_pg(lista) == True:
        resultado = "PG"
    if verifica_pa(lista) == False and verifica_pg(lista) == False:
        resultado = "NA"
    return resultado
  
    