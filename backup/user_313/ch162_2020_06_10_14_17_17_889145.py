def par_impar(x):
    if x%2 == 0:
        return "par"
    
    else:
        return "impar"
  
lista = list()

def verifica_lista(l1):
    
    par = False
    impar = False  
    if l1 == []:
        return 'misturado'
    
    if len(l1) < 2:
        x = par_impar(l1[0])
        if x == 'par':
            return 'par'
        elif x == 'impar':
            return 'impar'
        else:
            return 'misturado'
        
    
    for i in l1:
        x = par_impar(i)
        if x == "par":
            lista.append("par")
        
        if x == "impar":
            lista.append("impar")
    
      
    for i in lista:
        
        if i == 'par':
            par = True
        
        if i == 'impar':
            impar = True
               
    if par == True and impar == True:
        return 'misturado'
    
    if par == True and impar == False:
        return 'par'
    
    if impar == True and par == False:
        return 'impar'
    
print(verifica_lista([7,5]))
