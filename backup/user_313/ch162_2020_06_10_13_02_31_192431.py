def par_impar(x):
    if x % 2 == 0:
        return "par"
    
    else:
        return "impar"

Par = True
Impar = False
def verifica_lista(l1):
    if len(l1) == 0:
        return "misturado"
    
    for i in range(len(l1)-1):
        if len(l1) > 2: 
            resultado = par_impar(l1[i])
            resultado2 = par_impar(l1[i+1])
            
    if resultado == "par" and resultado2 == "par":
        return "par"
    
    elif resultado == "impar" and resultado2 == "impar":
        return "impar"
    
    else:
        return "misturado" 
    
    if len(l1) < 2:
        resultado = par_impar(l1[0])
        if resultado == "par":
            return "par"
        
        elif resultado == "impar":
            return "impar"