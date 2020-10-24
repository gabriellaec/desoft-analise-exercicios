from random import randint
lancamento1 = randint(2,20)
dinheiro = 10
pergunta = int(input("Digite um numero valido: "))
pergunta2 = int(input("Digite um numero maior que o anterior valido: "))
if lancamento1 < pergunta:
    print("Soma menor")
elif lancamento1 > pergunta2:
    print("Soma maior")
    