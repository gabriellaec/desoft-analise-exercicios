def eh_primo (x):
    if x <= 1:
        return False
    
    for i in range(2,x):
        if x%i == 0:
            return False
       
    return True

def maior_primo_menor_que (x):
    lista = [2]
    n_primo = 3