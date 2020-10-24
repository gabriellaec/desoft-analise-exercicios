cigarros_por_dia = input("Quantos cigarros voce fuma por dia? ")
anos_fumando = input("Há quantos anos voce fuma? ")

def calcula_tempo_de_vida_perdida(cigarros, anos):
    c = int(cigarros)
    a = int(anos)

    minutos_perdidos = c * 10
    horas_perdidas = minutos_perdidos / 60
    dias_perdidos = horas_perdidas / 24
    total_perdido = (a * 365) * dias_perdidos
    print(f'Voce perdeu {int(total_perdido)} dias')

calcula_tempo_de_vida_perdida(cigarros_por_dia, anos_fumando)