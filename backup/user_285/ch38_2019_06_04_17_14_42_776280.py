def eh_primo(num):
    if num<0:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
  
    return True
    
def primos_entre(a,b):
    listaprimos=[]
    for i in range(a,b+1):
        if eh_primo(i):
            listaprimos.append(i)
    return listaprimos
    