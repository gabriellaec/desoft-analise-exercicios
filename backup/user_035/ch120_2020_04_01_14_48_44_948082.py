import random
dinheiro = 100
while dinheiro!=0:
    print(dinheiro)
    resposta_aposta = input("Quer apostar? ")
    aposta_dinheiro = int(input("Quanto o senhor quer apostar? "))
    if aposta_dinheiro == 0 or resposta_aposta == "não":
        continue
        
    elif aposta_dinheiro>0 and aposta_dinheiro<=dinheiro:
        aposta_tipo = input("Qual o tipo de aposta ")
    
        if aposta_tipo == "n":
            resposta = int(input("Escolha um número entre 1 a 36: "))
            roleta = random.randint(1, 36)
            if resposta == roleta:
                dinheiro = dinheiro + aposta_dinheiro*35
                continue
            else:
                dinheiro = dinheiro - aposta_dinheiro
                continue
                
        elif aposta_tipo == "p":
            resposta = int(input("Escolha p ou i: "))
            roleta = random.randint(1, 2)
            if resposta == "p" and roleta == 2:
                dinheiro = dinheiro+aposta_dinheiro
                continue
            elif resposta == "i" and roleta == 1:
                dinheiro = dinheiro+aposta_dinheiro
                continue
            else:
                dinheiro = dinheiro-aposta_dinheiro
                continue
    else:
        continue