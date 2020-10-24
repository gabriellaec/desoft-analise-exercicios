import random
dado1= random.randint(1,6)
dado2= random.randint(1,6)
dado3= random.randint(1,6)
soma= dado1 + dado2 + dado3
dinheiro= 10
print("Você tem {} dinheiros" .format(dinheiro))
if dinheiro > 0:
    pergunta= str(input("Quer uma dica? (s/n) "))
    while pergunta == s:
        dinheiro= dinheiro-1
        Numero1= int(input("Digite um numero: "))
        Numero2= int(input("Digite um numero: "))
        Numero3= int(input("Digite um numero: "))
        if soma == Numero1 or Numero2 or Numero3:
            print("Está entre os 3")
        else:
            print("Não está entre os 3")
    elif dinheiro > 0:
        pergunta= str(input("Quer uma dica? (s/n) "))
        if pergunta == "s":
            dinheiro= dinheiro-1
            print("Você tem {} dinheiros" .format(dinheiro))