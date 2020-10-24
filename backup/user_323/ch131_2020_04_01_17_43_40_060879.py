import random
dados = random.randint(2,20)
dinheiro = 10
numero1 = int(input("escolha um numero de 0 a 10 "))
numero2 = int(input("Escolha um numero diferente, também de 0 a 10 "))
while numero1 == numero2:
    numero2 = int(input("mesmo número, tente de novo "))
soma = numero1+numero2
print(dados, soma)

