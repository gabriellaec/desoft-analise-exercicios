def calculo(num):
    num = int(input("Digite um inteiro [0 para terminar]: "))
    soma = 0

    while num != 0:
        soma = soma + num
        num = int(input("Digite um inteiro [0 para terminar]: "))

    print(soma)

