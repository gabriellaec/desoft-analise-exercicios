def eh_primo(numero):
    primopar = 2
    primeiroimpar = 3
    while numero % primopar != 0 and primeiroimpar < numero and numero % primeiroimpar !=0 and numero != 0 or numero == primopar or numero == 3:
        primeiroimpar += 2
        if primeiroimpar >= numero:
            return True
    return False

def lista_primos(intervalo1, intervalo2):
    lista = []
    i = 2
    while len(lista) < intervalo1 and len(lista) < intervalo2:
        if eh_primo(i):
            lista.append(i)
        i += 1
    return lista

def primos_entre(a, b):
    quantidade_lista = []
    t = 0
    while len(quantidade_lista) >= a and len(quantidade_lista) <= b:
        if lista_primos(a, b):
            quantidade_lista.append(len(lista_primos(a, b)))
        t += 1
    return quantidade_lista