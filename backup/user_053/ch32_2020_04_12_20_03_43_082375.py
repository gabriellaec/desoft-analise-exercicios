# Identifica se é primo ou não
def verifica_primo(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    elif n < 0: 
        return False
    else:
        for numero in range(3, n):
            if n %2 == 0:
                return False
            elif n %numero == 0:
                return False
        return True

# Define função que retorna primos
def lista_primos(numero):
    lista = []      # Lista de retorno
    elemento = 0    # Números para verificar se é ou não primo
    while len(lista) < numero:
        if verifica_primo(elemento):
            lista.append(elemento)
            elemento += 1
        else:
            elemento += 1
    return lista