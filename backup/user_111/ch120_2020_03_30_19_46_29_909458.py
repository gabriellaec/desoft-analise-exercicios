import random
dinheiro=100
def sorteia_numeros():
    numero=random.randint
    return numero

def n():
    global dinheiro
    aposta1=int(input("Digite um número de 1 a 36: "))
    aposta2=int(input("Quanto quer apostar? "))
    sorteio=sorteia_numeros()
    if aposta1==sorteio:
        dinheiro+=aposta2*35
        print("Você ganhou!")
    else:
        dinheiro-=aposta2
        print("Você perdeu! Está com",dinheiro,"dinheiros")
    
def p_ou_i():
    global dinheiro
    aposta1=int(input("Digite um número de 1 a 36: "))
    aposta2=int(input("Quanto quer apostar? "))
    sorteio=sorteia_numeros()
    if aposta1==sorteio:
        dinheiro+=aposta2
        print('Você ganhou!')
    else:
        dinheiro-=aposta2
        print("Você perdeu! Está com",dinheiro,"dinheiros")

jogar=True
pergunta=input("Você quer jogar? ")
if pergunta=="sim":
    jogar=True
elif pergunta=="não":
    jogar=False
    print("Ok!Volte depois!")
while jogar:
    print("Você começa com",dinheiro,"dinheiros")
    aposta=input("Selecione a aposta n ou p/i: ")
    if aposta=="n":
        n()
    elif aposta=="p" or "i":
        p_ou_i()