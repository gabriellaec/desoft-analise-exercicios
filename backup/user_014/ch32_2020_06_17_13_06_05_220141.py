# Definindo se um número é primo
def eh_primo (n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    else:
        if n % 2 == 0:
            return False
        else:
            for i in range(3, n, 2):
                if n % 2 == 0:
                    return False
                elif n % i == 0:
                    return False
            return True

lista_n = []
def lista_primos(x):
    x == len(lista(n))
    for i in lista_n:
        lista_n.append(eh_primo(n))
    return lista_n