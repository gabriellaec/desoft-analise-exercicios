macos= int(input("Quantos cigarros por dia? "))

tempo= int(input("Quantos anos fuma? "))

#1 cigarro 10min de vida    #1 dia= 24*60 min

def perdido (macos,tempo):
    m=macos*10*365*tempo  #minutos perdidos nos anos de fumo
    dia= m/(24*60)
    return dia

vida= perdido(macos,tempo)

print("Tempo perdido: {0} dias".format(vida))