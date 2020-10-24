pergunta = float(input("Digite um número: "))
while True:
    if pergunta != 0:
        soma = soma + pergunta
        pergunta = float(input("Digite um número: "))
        index = index + 1
    else:
        print(soma)