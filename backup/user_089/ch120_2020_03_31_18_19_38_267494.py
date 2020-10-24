import random
d = 100
i = 0

print("quantidade de dinheiro disponível:",d)

V = int(input("Aposte um valor:"))

if V == 0:
    print("Erro.")

aposta = input("A aposta é em um número(n) ou paridade(p)?")
if aposta == "n":
    sorteio_n = random.randint(0,36)
    numero = int(input("Digite um número de 1 a 36:"))
    if numero == sorteio_n:
        ganhou_n = 100 + V *35
        print(ganhou_n)
    else:
        perdeu_n = 100 - V
        print(perdeu_n)
if aposta == "p":
    sorteio_p = random.randint(n,p)
    opcao = int(input("Você escolhe par(p) ou ímpar(i)?:"))
    if opcao == sorteio_p:
        acerto = 100 + V
        print(acerto)
    if opcao != sorteio_p:
        erro = 100 - V
        print(erro)