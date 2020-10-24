def eh_primo(n):
    if n == 2 or n ==3:
        return True
    if n == 0 or n ==1:
        return False
    i = 3
    while i < n:
        if n%i == 0 or n%2 == 0:
            return False
        i = i+2
    else:
        return True
        
def maior_primo_menor_que(n):
    lista = [2]
    n_primo = 3
    if n < 2:
        return -1
    if eh_primo(n) == True:
        return n
    if eh_primo(n) == False:
        if n < 2:
            return -1
        else:
            while lista[-1] < n:
                for x in range(2, n_primo):
                    if n_primo%x == 0:
                        break
                    if x == (n_primo - 1):
                        lista.append(n_primo)
                n_primo += 1
            return lista[-2]
                    

