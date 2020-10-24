def par_impar(x):
    if x%2 == 0:
        return "par"
    
    else:
        return "impar"
  
lista = list()
def verifica_lista(l1):
    if l1 == []:
        return "misturado"
    
    for i in l1:
        x = par_impar(i)
        if x == "par":
            lista.append("par")
        
        elif x == "impar":
            lista.append("impar")
    
    par = False
    impar = False        
    for i in lista:
        if i == 'par':
            par = True
        
        elif i == 'impar':
            impar == True
        
    if par and impar:
        return misturado
    
    elif par and not impar:
        return "par"
    
    elif impar and not par:
        return 'impar'