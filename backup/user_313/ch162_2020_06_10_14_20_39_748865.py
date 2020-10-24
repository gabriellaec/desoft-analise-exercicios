def par_impar(x):
    if x%2 == 0:
        return "par"
    
    else:
        return "ímpar"
  


def verifica_lista(l1):
    lista = list()
    par = False
    impar = False  
    if l1 == []:
        return "misturado"
    
    if len(l1) < 2:
        x = par_impar(l1[0])
        if x == 'par':
            return 'par'
        elif x == "ímpar":
            
            return "ímpar"
        else:
            return 'misturado'
        
    
    for i in l1:
        x = par_impar(i)
        if x == "par":
            lista.append("par")
        
        if x == "ímpar":
            lista.append("ímpar")
    
      
    for i in lista:
        
        if i == 'par':
            par = True
        
        if i == "ímpar":
            impar = True
               
    if par == True and impar == True:
        return "misturado"
    
    if par == True and impar == False:
        return "par"
    
    if impar == True and par == False:
        return "ímpar"

