def primos_entre(a,b):
    quantidade_de_primos = 0
    while a <= b:
        if eh_primo(a):
            quantidade_de_primos += 1
        a+=1

    return quantidade_de_primos