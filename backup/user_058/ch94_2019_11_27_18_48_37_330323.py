v = float(input("Qual a velocidade permitida na pista(em km/h)? "))
d = float(input("Qual a distância entre as duas câmeras(em metros)? "))

distancia = d/1000
while True:
    placa = str(input("Digite a combinação alfanumérica da placa: "))
    if placa == None:
        break
    instante_inicial = float(input('Qual o instante em segundos em que o carro passou pela camera 1? '))
    instante_final = float(input('Qual o instante em segundos em que o carro passou pela camera 2? '))
    t = (instante_final - instante_inicial)
    tempo = t/3600
    velocidade_por_hora = distancia/tempo
    if velocidade_por_hora <= v:
        print("Você não cometeu infração")
        print('Sua multa é de: R$0,00')
    elif velocidade_por_hora > v and <= (v*1.2):
        print("Você cometeu uma infração média")
        print("Sua multa é de: R$130,16")
    elif velocidade_por_hora > (v*1.2) and velocidade_por_hora <= (v*1.5):
        print("Você cometeu uma infração grave")
        print("Sua multa é de: R$195,23")
    elif velocidade_por_hora > (v*1,5):
        print("Você cometeu uma infração gravíssima")
        print("Sua multa é de: 3x R$130,16")
        print("Seu documento de habilitação será apreendido e você recebeu suspenção imediata do seu direito de dirigir")
