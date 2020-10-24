pergunta1 = int(input("Quantos cigarros vc fuma por dia? "))
pergunta2 = int(input("Há quantos anos vc fuma? "))

def temp_perdido(cigarro,ano):
    minutos_perdidos = cigarro*10
    dias_perdidos = (minutos_perdidos/60)/24
    dias_fumando = ano*365
    vida_perdida = anos_perdidos*dias_fumando
    return vida_perdida

morreu = temp_perdido(pergunta1,pergunta2)

print("Vc perdeu {0} anos de vida fumando!".format(morreu))