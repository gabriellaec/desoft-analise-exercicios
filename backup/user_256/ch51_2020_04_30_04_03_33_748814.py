def eh_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    for i in range(3, n, 2):
        if n%2==0:
            return False
        elif n%i==0:
            return False
    else:
        return True
        
            
def primos_entre(a, b):
    cont=0
    lista=[]
    while cont<=b:
        cont=a
        if eh_primo(a):
            lista.append(cont)
        a+=1
    print(lista)
    return lista


            
        

    
            
        