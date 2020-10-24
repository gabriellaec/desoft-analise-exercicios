pergunta1 = int(input("Digite a quantidade de dias: "))
pergunta2 = int(input("Digite a quantidade de horas: "))
pergunta3 = int(input("Digite a quantidade de minutos: "))
pergunta4 = int(input("Digite a quantidade de segundos: "))

def transforma_segundo(d,h,m,s):
    segundos = d*24*60*60 + h*60*60 + m*60 + s
    return segundos

segundos_transf = transforma_segundo(pergunta1,pergunta2,pergunta3,pergunta4)

print("O total de segundos é: {0}".format(segundos_transf))