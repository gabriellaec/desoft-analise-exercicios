def lista_primos (n):
    if n == 2:
        return True 
    elif n == 0 or n == 1:
        return False 
    elif n%2 == 0:
        return False 
    else:
        contador = 3
        while contador < n:
            if n%contador == 0: 
                return False 
            contador +=2
        return True
    
def lista_primos (q):
    i=0
    listap=[]
    while len(listap)<q:
        if eh_primos(i)= True:
            listap.append(i)
            i+=1
        else:
            i+=1
    return listap