import random
moedas = 100  #Quantidade inicial de moedas
print ("Bem-vindo ao jogo da Roleta simplificado!")
JOGO = True
while JOGO and moedas >0:  #O jogo vai rodar enquanto ele tiver moedas. (obs: moedas pode ficar negativo)
    #Condições de análise da continuidade do jogo
    print ("Você tem {0} moedas" .format(moedas))
    valor_aposta = int(input ("Aposte um valor para poder jogar: "))
    # Fazer sair do jogo, caso valor_aposta = 0.
    if valor_aposta == 0:
        JOGO = False
    #Escolhendo o tipo de jogo
    tipo_de_jogo = 'x'
    if JOGO:
        tipo_de_jogo = input("Você quer apostar em um número (digite 'n') ou em paridade (digite 'p') ? ")
    #Aposta em números
    if tipo_de_jogo == 'n' and JOGO:
        dado = random.randint(0,36)
        aposta_numero = int(input("Digite um número de 0 a 36 para usar como aposta"))
        if aposta_numero == dado:
            print ("Parabéns! Você acertou o número!")
            moedas += 35*valor_aposta
        else: 
            print ("Você errou!")
            moedas -= valor_aposta
    #Aposta em paridade        
    elif tipo_de_jogo == 'p' and JOGO:
        aposta_paridade = input("Digite 'p' para escolhar PAR ou 'i' para escolher ÍMPAR ")
        dado = random.randint(0,36)
        resultado = 'x'
        if dado%2 == 0:
            resultado = 'p'
        else:
            resultado = 'i'
        if aposta_paridade == resultado:
            print ("Parabéns! Você acertou!")
            moedas += valor_aposta
        else: 
            print ("Você errou!")
            moedas -= valor_aposta

#FIM DE JOGO   
print ("Fim de Jogo. Você permaneceu com {0} moedas. Obrigado!" .format(moedas))