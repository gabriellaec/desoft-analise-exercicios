import random
dinheiro=100
def sorteia_numeros():
    numero=random.randint(0,36)
    return numero

def n():
    global dinheiro
    aposta1=int(input("Digite um número de 1 a 36: "))
    aposta2=int(input("Quanto quer apostar? "))
    sorteio=sorteia_numeros()
    if aposta1==dinheiro and aposta1!=sorteio:
        print(dinheiro)
    elif aposta1==sorteio:
        dinheiro+=aposta2*35
        print("Você ganhou!")
    else:
        dinheiro-=aposta2
        print("Você perdeu! Está com",dinheiro,"dinheiros")
    
def p_ou_i():
    global dinheiro
    pergunta=input("Você quer p ou i?")
    aposta1=int(input("Digite um número de 1 a 36: "))
    aposta2=int(input("Quanto quer apostar? "))
    sorteio=sorteia_numeros()
    if aposta1==dinheiro and aposta1!=sorteio:
        print(dinheiro)
    elif aposta1==sorteio:
        dinheiro+=aposta2
        print(dinheiro)
    else:
        dinheiro-=aposta2
        print(dinheiro)

print(dinheiro)
aposta=input("Selecione a aposta n ou p/i: ")
if aposta=="n":
    n()
elif aposta=="p" or "i":
    p_ou_i()