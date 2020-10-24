import random
dinheiro=100
def sorteia_numeros():
    numero=random.randint
    return numero

def n():
    global dinheiro
    aposta1=int(input("Quanto quer apostar? "))
    aposta2=int(input("Digite um número de 1 a 36"))
    sorteio=sorteia_numeros()
    if aposta2==sorteio:
        dinheiro+=aposta1*35
        print("Você ganhou!")
    else:
        dinheiro-=aposta1
    
def p_ou_i():
    global dinheiro
    aposta1=int(input("Quanto quer apostar? "))
    aposta2=int(input("Digite um número de 1 a 36"))
    sorteio=sorteia_numeros()
    if aposta2==sorteio:
        dinheiro+=aposta1
        print('Você ganhou!')
    else:
        dinheiro-=aposta1


print("Você começa com",dinheiro,"dinheiros")
aposta=input("Selecione a aposta n ou p/i: ")
if aposta=="n":
    n()
elif aposta=="p" or "i":
    p_ou_i()