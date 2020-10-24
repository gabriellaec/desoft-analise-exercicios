d=float(input("Qual a distância que você deseja percorrer em km?"))
def preco_passagem(d):
    if d<=200:
        p=d*0.5
        return p
    else:
        p=((d-200)*0.45+100)
        return p
print("Preço da passagem{0:.2f}".format(preco_passagem(d)))

