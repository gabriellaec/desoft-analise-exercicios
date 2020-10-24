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
    if eh_primo(x) == True:
        return x
    if eh_primo(x) == False:
        if n < 2:
            return -1
        else:
            while lista[-1] < n:
                for x in range (2,n_primo):
                    if n_primo%x == 0:
                    break
                    if x == (n_primo - 1):
                    lista.append(n_primo)
                n_primo += 1
            return lista[-2]