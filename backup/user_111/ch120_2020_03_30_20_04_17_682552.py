import random
dinheiro=100
def sorteia_numeros():
    numero=random.randint(0,36)
    return numero

def n(aposta2):
    global dinheiro
    sorteio=sorteia_numeros()
    aposta1=int(input("Digite um número de 1 a 36: "))
    if aposta1==dinheiro and aposta1!=sorteio:
        print(dinheiro)
    elif aposta1==sorteio:
        dinheiro+=aposta2*35
        print(dinheiro)
    else:
        dinheiro-=aposta2
        print(dinheiro)
    
def p_ou_i(aposta2):
    global dinheiro
    sorteio=sorteia_numeros()
    pergunta=input("Você quer p ou i?")
    aposta1=int(input("Digite um número de 1 a 36: "))
    if aposta1==dinheiro and aposta1!=sorteio:
        print(dinheiro)
    elif aposta1==sorteio:
        dinheiro+=aposta2
        print(dinheiro)
    else:
        dinheiro-=aposta2
        print(dinheiro)

jogar=True
while jogar:
    if quer_jogar=="não":
        jogar=False
    print(dinheiro)
    sorteio=sorteia_numeros()
    aposta2=int(input("Quanto quer apostar? "))
    aposta=input("Selecione a aposta n ou p/i: ")
    if aposta2==dinheiro and aposta2!=sorteio:
            print(dinheiro)
    if aposta=="n":
        n(aposta2)
    elif aposta=="p" or "i":
        p_ou_i(aposta2)