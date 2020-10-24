pergunta1 = int(input("Quantos cigarros vc fuma por dia? "))
pergunta2 = int(input("A quantos anos vc fuma? "))

def temp_perdido(c,a):
    anos_perdidos = ((c*10)/(60/24))*a
    return anos_perdidos

morreu = temp_perdido(pergunta1,pergunta2)

print("Vc perdeu {0} anos de vida fumando!".format(morreu))