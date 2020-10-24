import random
dinheiro=100
def sorteia_numeros():
    numero=random.randint(0,36)
    return numero

def n():
    global dinheiro
    sorteio=sorteia_numeros()
    if aposta1==dinheiro and aposta1!=sorteio:
        print(dinheiro)
    aposta1=int(input("Digite um número de 1 a 36: "))
    aposta2=int(input("Quanto quer apostar? "))
    if aposta1==sorteio:
        dinheiro+=aposta2*35
        print("Você ganhou!")
    else:
        dinheiro-=aposta2
        print("Você perdeu! Está com",dinheiro,"dinheiros")
    
def p_ou_i():
    global dinheiro
    sorteio=sorteia_numeros()
    pergunta=input("Você quer p ou i?")
    if aposta1==dinheiro and aposta1!=sorteio:
        print(dinheiro)
    aposta1=int(input("Digite um número de 1 a 36: "))
    aposta2=int(input("Quanto quer apostar? "))
    if aposta1==sorteio:
        dinheiro+=aposta2
        print(dinheiro)
    else:
        dinheiro-=aposta2
        print(dinheiro)

print(dinheiro)
sorteio=sorteia_numeros()
aposta1=int(input("Quanto quer apostar? "))
aposta=input("Selecione a aposta n ou p/i: ")
if aposta1==dinheiro and aposta1!=sorteio:
        print(dinheiro)
if aposta=="n":
    n()
elif aposta=="p" or "i":
    p_ou_i()