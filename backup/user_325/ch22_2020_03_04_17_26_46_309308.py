numero = int(input("quantos cigarros fuma por dia? "))
anos = int(input("ha quantos anos fuma? "))
def cigarro(numero,anos):
    c = (((anos*365)*numero)*10)/24
    return c
