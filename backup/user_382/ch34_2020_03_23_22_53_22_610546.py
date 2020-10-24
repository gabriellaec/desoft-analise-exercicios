def eh_primo(num):
    div = 3 
    if num % 2 == 0 and num != 2 or num == 1 or num == 0:
        return False
    
    while num > div:
        if num % div == 0:
            return False
        div += 2 
    return True 

def maior_primo_menor_que(n):
    lista = []
    if n <= 2:
        return -1
    for i in range(n):
        if eh_primo(i) == True:
            lista.append
    return max(lista)
            