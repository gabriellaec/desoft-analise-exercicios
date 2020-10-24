cigarros=int(input("quantos cigarros fuma por dia?"))
anos=int(input("quantos anos?"))

def tempo_perdido(cigarros,anos):
    t=int(anos)*365*int(cigarros)*1/144
    return t
