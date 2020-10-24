num = int(input("Digite um inteiro: "))
def calculo(num):
    soma = 0
    while (num != 0):
        soma += num
        num = int(input("Digite um inteiro: "))
    return soma