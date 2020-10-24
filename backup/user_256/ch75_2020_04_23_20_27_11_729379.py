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
        
def verifica_primos(lista):
    lista_pra_t_ou_f = {}
    for numeros in lista:
        if eh_primo[numeros]:
            lista_pra_t_ou_f[numeros] = True
        else:
            lista_pra_t_ou_f[numeros] = False
    return lista_pra_t_ou_f
    