#Com for
def soma_valores (valores):
    s = 0
    for i in range(len(valores)):
        s = s + valores[i]
    return s

#Com while
def soma_valores (valores):
    # Determina uma variável com o valor inicial da soma
    s = 0
    i = 0
    while i< len(valores):
        # Atualiza o valor da soma para cada elemento da lista
        s = s + valores[i]
        i= i +1
    return s
