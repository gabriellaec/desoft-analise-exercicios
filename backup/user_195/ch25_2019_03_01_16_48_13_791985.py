pergunta=int(input("Quantos quilometros você deseja percorrer?"))
if pergunta<=200:
    a=0.5*pergunta
    return a
else:
    a=100+(0.45*(pergunta-200))
    return a
print("O preço da passagem é {:.2f}".format(a))