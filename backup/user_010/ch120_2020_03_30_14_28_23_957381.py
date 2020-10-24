import random
dinheiro = 100
roleta = True

while roleta:
    
    print ("Você tem {} dinheiros.".format (dinheiro))
    aposta = int (input("Faça sua aposta: "))
    bolinha = random.randint (0,36)
    
    if aposta == 0 or aposta > dinheiro:
        print ("O programa parou.")
        roleta=False
    else:
        tipo = str (input (" 'n' para apostar em Número ou 'p' para apostar em Paridade: "))
        if tipo == "n":
            numero = int (input ("Escolha um número de 1 a 36: "))
            if numero == bolinha:
                dinheiro = dinheiro + (35*aposta)
                print ("Você ganhou!")
            elif numero != bolinha:
                dinheiro = dinheiro - aposta
                print ("Você perdeu!")
            
        elif tipo == "p":
            paridade = str(input("Par (p) ou Ímpar (i)? "))
            
            if paridade == "p":
                if bolinha%2==0 or bolinha==0:
                    dinheiro = dinheiro + aposta
                    print ("Você ganhou!")
                elif bolinha%2!=0:
                    dinheiro = dinheiro - aposta
                    print ("Você perdeu!")
                    
            elif paridade == "i":
                if bolinha%2!=0:
                    dinheiro = dinheiro + aposta
                    print ("Você ganhou!")
                elif bolinha%2==0 or bolinha==0:
                    dinheiro = dinheiro - aposta
                    print ("Você perdeu!")
                    
        print (bolinha)