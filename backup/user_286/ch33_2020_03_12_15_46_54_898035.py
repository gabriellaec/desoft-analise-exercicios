def eh_primo (numero):
    if numero == 1 or numero == 0:
        return False
    elif numero == 2:
        return True
    else:
        div = 2
        cont = 0
        while div < numero:
            if numero % div == 0:
                cont += 1
            div += 1
        if cont == 0:
            return True
        else:
            return False

def lista_primos (n):
    cont_teste = 0
    lista = []
    lista_modelo = [0]*n
    while len(lista) != len(lista_modelo):
        if eh_primo(cont_teste) == True:
            lista.append(cont_teste)
        cont_teste += 1

    return lista

def primos_entre (a,b):
    lista_1 = lista_primos(b)

    lista_final = [i for i in lista_1 if i >= a and i <= b]

    return lista_final

print(primos_entre(2,100))