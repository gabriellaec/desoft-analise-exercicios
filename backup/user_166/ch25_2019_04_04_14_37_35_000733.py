x=int(input("Qual a distância em km?"))
def preco_passagem(x):
    if x>=200:
        preço=0.50*200 + 0.45*(x-200)
    return "preço {0:.2f}".format(preço)
        