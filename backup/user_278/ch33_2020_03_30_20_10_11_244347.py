def primos_entre(a,b):
    quantidade_de_primos = 0
    x = a
    while x <= b:
        if eh_primo(x):
            quantidade_de_primos += 1
        x += 1

    return quantidade_de_primos