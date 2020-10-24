def eh_primo(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return False
                break
        else:
            return True

    else:
        return False

def verifica_primos(lista):
    dic={}
    for i in lista:
        dic[i]=eh_primo(i)
    return dic
        
    