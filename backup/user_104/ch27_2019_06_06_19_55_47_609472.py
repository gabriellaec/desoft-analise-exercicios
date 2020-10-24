cigarros = int(input('Quantos cigarros voce fuma por dia?'))
anos = int(input('Há quantos anos você fuma?'))
def conta_vida(cigarros, anos):
    tempo_perdido = ((cigarros*10)/1440)*(anos*365)
    return tempo_perdido
print(conta_vida(cigarros, anos))