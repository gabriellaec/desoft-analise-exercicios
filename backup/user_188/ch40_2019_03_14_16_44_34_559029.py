def fatorial(numero):
    resultado = 1
    if numero == 0:
        print(resultado)
    else:
        while numero > 0:
            resultado = resultado * numero
            numero -=1
        print(resultado)