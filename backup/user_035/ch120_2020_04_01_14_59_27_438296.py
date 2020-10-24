import random
dinheiro = 100
while dinheiro!=0:
    print(dinheiro)
    resposta_aposta = input("Quer apostar? ")
    aposta = int(input("Quanto o senhor quer apostar? "))
    if aposta == 0:
        continue
    elif resposta_aposta == não:
        break
        
    elif aposta>0 and aposta<=dinheiro:
        aposta_tipo = input("Qual o tipo de aposta ")
    
        if aposta_tipo == "n":
            resposta = int(input("Escolha um número entre 1 a 36: "))
            roleta = random.randint(1, 36)
            if resposta == roleta:
                dinheiro = dinheiro + aposta*35
                continue
            else:
                dinheiro = dinheiro - aposta
                continue
                
        elif aposta_tipo == "p":
            resposta = int(input("Escolha p ou i: "))
            roleta = random.randint(1, 2)
            if resposta == "p" and roleta == 2:
                dinheiro = dinheiro+aposta
                continue
            elif resposta == "i" and roleta == 1:
                dinheiro = dinheiro+aposta
                continue
            else:
                dinheiro = dinheiro-aposta
                continue
    else:
        continue
print("Perdeu")