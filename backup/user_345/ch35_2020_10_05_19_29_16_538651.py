def calculo(num):
    num = int(input("Digite um inteiro: "))
    soma = 0
    while (num != 0):
        soma = soma + num
        num = int(input("Digite um inteiro: "))
    return soma