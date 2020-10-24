def eh_primo(x):
    if(x == 0 or x == 1):
        return(False)
    if (x == 2):
        return(True)
    if (x%2 == 0):
        return(False)
    
    a = 3
    while a < x:
        if x%a ==0:
            return(False)
        else:
            a = a + 2
    return(True)

def primos_entre(a,b):
    numero = a 
    contador = 0
    lista = []
    y = True
    while y:
        
        if (eh_primo(numero) == True and numero <= b):
            lista.append(numero)
            
            
        numero = numero + 1
        contador = contador + 1
        
        if contador == b:
            return(len(lista))
            y = False

print(primos_entre(2,3))