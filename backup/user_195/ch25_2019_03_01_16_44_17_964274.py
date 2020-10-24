pergunta=int(input("Quantos quilometros você deseja percorrer?"))
if pergunta<=200:
    a=0.5*pergunta
    return a
else:
    b=a+ (0.45*(pergunta-200))
    return b