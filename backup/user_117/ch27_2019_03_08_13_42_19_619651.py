cigarros=int(input("quantos cigarros fuma por dia?"))
anos=int(input("quantos anos?"))
def tempo_perdido(cigarros,anos):
    t=anos*365*cigarros*1/144
    return t
