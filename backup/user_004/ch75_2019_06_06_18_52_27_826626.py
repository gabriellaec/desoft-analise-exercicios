def primo(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n == 5:
        return False
    elif n == 3:
        return True
    elif n % n == 0 and n % 1 == 0 and n % 2 == 0:
        return False
    elif n % n == 0 and n % 1 == 0 and n % 5 == 0:
        return False
    elif n % n == 0 and n % 1 == 0 and n % 3 == 0:
        return False
    else:
        return True


def verifica_primos(lista):
    dic = {}
    i = 0
    while i < len(lista):
        if primo(lista[i]) == True:
            dic[lista[i]] = True
        else:
            dic[lista[i]] = False
        i += 1
    return dic

print(verifica_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))