def calcula_tempo(n):
    dicionario2 = {}
    for k, v in n.items():
        dicionario2[k] = ((200/v)**(1/2))
    return dicionario2

n = {}
nome = input("Qual o nome")
aceleracao = float(input("Qual a aceleracao"))
while nome != "sair":
    n[nome] = aceleracao
    nome = input("Qual o nome")
    if nome == "sair":
        break
    aceleracao = float(input("Qual a aceleracao"))
    
tempo = calcula_tempo(n)
maior = 0
for k, v in tempo.items():
    if v > maior:
        nome = k
        maior = v
print("O vencedor é",k, "com tempo de conclusão de", v,"s")