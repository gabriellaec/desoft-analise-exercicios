def primos_entre(a,b):
    lista = []
    i = a
    while i<=b:
        if eh_primo(i) == True:
            lista.append(i)
        i+=1
    return len(lista)