import random
dinheiro = 100
resetar = True
while dinheiro!=0 or resetar == True:
    print(dinheiro)
    
    aposta_dinheiro = int(input("Quanto o senhor quer apostar? "))
    if aposta == 0:
        resetar = True
        
    elif aposta>0 and aposta<=dinheiro:
        aposta_tipo = input("Qual o tipo de aposta ")
    
        if aposta_tipo == "n":
            resposta = int(input("Escolha um número entre 1 a 36: "))
            roleta = random.randint(1, 36)
            if resposta == roleta:
                dinheiro = dinheiro + aposta_dinheiro*35
                resetar = True
            else:
                dinheiro = dinheiro - aposta_dinheiro
                resetar = True
                
        elif aposta_tipo == "p":
            resposta = int(input("Escolha p ou i: "))
            roleta = random.randint(1, 2)
            if resposta == "p" and roleta == 2:
                dinheiro = dinheiro+aposta_dinheiro
                resetar = True
            elif resposta == "i" and roleta == 1:
                dinheiro = dinheiro+aposta_dinheiro
                resetar = True
            else:
                dinheiro = dinheiro-aposta_dinheiro
                resetar = True
    else:
        resetar = True