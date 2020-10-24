import random
d = 1000
perg = True
while perg:
    perg = input("Você quer apostar?")
    if perg == "não":
        perg = False
    else:
        a = random.randint(1,6)
        b = random.randint(1,6)
        z = a + b
        if jogador == z:
            d = d + 20
        else:
            d = d -30
            siri2 = input ("Você vai continuar tentando ou vai desistir?")
            if siri2 == "desistir":
                perg = True
            else:
                sire = input("Chute um número:")
                if sire == z:
                    d = d + 30
                elif sire != z:
                    computador = input (f"O valor de um dos dados é {a}. Você quer continuar ou desistir?")
                    if computador == "desistir":
                        perg = True
                    elif computador == "continuar":
                        computador2 = input("Digite mais um número para acertar o valor:")
                            if computador2 == z:
                                d = d - 10
                            elif:
                                perg = True
        
                        
                
            
    
