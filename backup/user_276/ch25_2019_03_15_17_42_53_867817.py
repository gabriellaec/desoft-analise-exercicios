dist = int(input("Qual é a distância que você quer percorrer em km?"))
def calcula_preco(dist):
    if dist <= 200:
        return dist*0.50
    else:
        return 100 + dist*0.45
a = (calcula_preco(200))
print(a)