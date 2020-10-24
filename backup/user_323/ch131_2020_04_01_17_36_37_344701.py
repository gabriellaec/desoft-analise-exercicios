dados = [1,2,3,4,5,6,7,8,9,10]
dinheiro = 10
numero1 = int(input("escolha um numero de 0 a 10 "))
numero2 = int(input("Escolha um numero diferente, também de 0 a 10 "))
while numero1 == numero2:
    numero2 = int(input("mesmo número, tente de novo "))
soma = numero1+numero2