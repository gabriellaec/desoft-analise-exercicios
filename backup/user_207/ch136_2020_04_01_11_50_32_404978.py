import random

dinheiros = 10

d1 = random.randint(1,6)
d2 = random.randint(1,6)
d3 = random.randint(1,6)


soma = d1+d2+d3

print (soma)
JOGO = False

#fase de DICAS
print ("DICAS: \n Você possui {0} dinheiros." .format(dinheiros))
if dinheiros <=0:
    print ("Você perdeu!")
else: 
    pergunta1 = input("Você quer uma dica? ")
    if pergunta1 == 'sim':
        dinheiros -= 1
        perguntaA = int(input ("Me diga um valor possível para a soma "))
        perguntaB = int(input ("Me diga outro valor possível para a soma "))
        perguntaC = int(input ("Me diga outro valor possível para a soma "))
        if perguntaA == soma:
            print ("Está entre os 3")
        elif perguntaB == soma:
            print ("Está entre os 3")
        elif perguntaC == soma:
            print ("Está entre os 3")
        else:
            print ("Não está entre os 3")
JOGO = True
        
while JOGO:
        
        if dinheiros <=0:
            print ("Você perdeu!")
            JOGO = False
        else: 
            print(" {0} dinheiros" .format(dinheiros))
            resposta = int(input ("Qual o valor da soma?"))
            if resposta == soma:
                dinheiros += 5*dinheiros
                print ("Você ganhou o jogo com {0} dinheiros" .format (dinheiros))
                JOGO = False
            else:
                dinheiros -= 1