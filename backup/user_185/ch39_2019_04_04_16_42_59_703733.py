pergunta = float(input("Digite um número: "))
soma = 0
index = 0
while True:
    if pergunta != 0:
        soma = soma + pergunta
        pergunta = float(input("Digite um número: "))
        index = index + 1
    else:
        break
print(soma)