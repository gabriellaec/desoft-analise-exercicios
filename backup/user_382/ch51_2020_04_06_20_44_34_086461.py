def eh_primo(num):
    div = 3 
    if num < 2:
        return False
    if num % 2 == 0 and num != 2 or num == 1 or num == 0 or num == -1:
        return False
    
    while num > div:
        if num % div == 0:
            return False
        div += 2 
    return True 

def primos_entre(a,b):
    lista = []
    for i in range(a,b+1):
        if eh_primo(i) == True:
            lista.append(i)
    sorted(lista)
    return lista 