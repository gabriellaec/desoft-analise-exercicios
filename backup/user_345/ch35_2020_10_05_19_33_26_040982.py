def calculo(num):
    soma = 0
    num = int(input("Digite um inteiro: "))
    while (num != 0):
        soma += num
        num = int(input("Digite um inteiro: "))
    return soma