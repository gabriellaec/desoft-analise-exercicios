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

def maior_primo_menor_que(n):
    numero = n
    contador = 0
    lista = []
    y = True
    while y:

        if n <= 1:
            return(-1)
            y = False
        if n == 2:
            return(2)

        if (eh_primo(numero) == True and numero <= n):
            lista.append(numero)
            
            
            
        elif (eh_primo(numero) ==  False)
            numero = numero - 1
            
        contador = contador + 1

        
        if contador > n:
            return lista[1]
            y = False
            
