from random import randint
dinheiro=100
aposta = int(input("Digite um valor: "))
while aposta!=0 and dinheiro>0:
    tipo = input("Numero ou paridade: ")
    if tipo == 'n':
        numero=int(input("Digite um número de 1 a 36: "))
        if numero == randint(0,36):
            dinheiro=dinheiro+35*aposta
            print(dinheiro)
            if dinheiro>0:
                aposta = int(input("Digite um valor: "))
        else:
            dinheiro=dinheiro-aposta
            print(dinheiro)
            if dinheiro>0:
                aposta = int(input("Digite um valor: "))
    elif tipo == "p":
        impar_ou_par=input("Digite i ou p" )
        numero_sorteado=randint(0,36)
        if impar_ou_par== "i":
            if numero_sorteado%2==0 or numero_sorteado==0:
                dinheiro=dinheiro-aposta
                print(dinheiro)
                if dinheiro>0: 
                    aposta = int(input("Digite um valor: "))
            else:
                dinheiro=dinheiro+aposta
                print(dinheiro)
                if dinheiro>0:
                    aposta = int(input("Digite um valor: "))
        elif impar_ou_par == "p":
            if numero_sorteado%2==0 or numero_sorteado==0:
                dinheiro=dinheiro+aposta
                print(dinheiro)
                if dinheiro>0: 
                    aposta = int(input("Digite um valor: "))
            else:
                dinheiro=dinheiro-aposta
                print(dinheiro)
                if dinheiro>0:
                    aposta = int(input("Digite um valor: "))