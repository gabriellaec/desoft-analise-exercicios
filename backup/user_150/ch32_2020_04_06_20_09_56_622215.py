def eh_primo(numero):
    primopar = 2
    primeiroimpar = 3
    while numero % primopar != 0 and primeiroimpar < numero and numero % primeiroimpar !=0 and numero != 0 or numero == primopar or numero == 3:
        primeiroimpar += 2
        if primeiroimpar >= numero:
            return True
    return False
def lista_primos(intervalo):
    lista = []
    i = 2
    while len(lista) <= intervalo: 
        if eh_primo(i):
            lista.append(i)
        i += 1
    return lista