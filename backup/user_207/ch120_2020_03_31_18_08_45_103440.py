import random
moedas = 100  #Quantidade inicial de moedas
print ("Bem-vindo ao jogo da Roleta simplificado!")
fim_de_jogo = 1
while moedas and fim_de_jogo > 0:  #O jogo vai rodar enquanto ele tiver moedas. (obs: moedas pode ficar negativo)
    print ("Você tem {0} moedas" .format(moedas))
    valor_aposta = int(input ("Aposte um valor para poder jogar: "))
    if valor_aposta == 0:
        fim_de_jogo =0
    tipo_de_jogo = input("Você quer apostar em um número (digite 'n') ou em paridade (digite 'p') ? ")
    if tipo_de_jogo == 'n':
        dado = random.randint(1,36)
        aposta_numero = int(input("Digite um número de 1 a 36 para usar como aposta"))
        if aposta_numero == dado:
            print ("Parabéns! Você acertou o número!")
            moedas += 35*valor_aposta
        else: 
            print ("Você errou!")
            moedas -= valor_aposta
    elif tipo_de_jogo == 'p':
        aposta_paridade = input("Digite 'p' para escolhar PAR ou 'i' para escolher ÍMPAR ")
        dado = random.randint(1,36)
        resultado = 'x'
        if dado%2 == 0:
            resultado = 'p'
        else:
            resultado = 'i'
        if aposta_numero == resultado:
            print ("Parabéns! Você acertou!")
            moedas += valor_aposta
        else: 
            print ("Você errou!")
            moedas -= valor_aposta

   
print ("Obrigado! Tchau!")