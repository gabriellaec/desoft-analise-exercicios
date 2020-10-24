distancia=float(     input("Qual a distância em km que você deseja percorrer?")    )

def preço_da_passagem(x):
    if x <= 200:
        y=0.5*x
    else:
        y=100+0.45*(x-200)
    return y

resultado = float((preço_da_passagem(distancia)))


print ("{0:.2f}".format(resultado))