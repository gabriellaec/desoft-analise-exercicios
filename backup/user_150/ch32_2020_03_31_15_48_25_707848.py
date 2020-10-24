def lista_primos(intervalo):
    lista = []
    def eh_primo(numero):
        primopar = 2
        primeiroimpar = 3
        while numero % primopar != 0 and primeiroimpar < numero and numero % primeiroimpar != 0 and numero != 0 or numero == primopar or numero == 3:
            primeiroimpar += 2
            if primeiroimpar >= numero:
                lista.append(numero)
                return numero
        return False