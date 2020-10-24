pergunta = float(int("qual distância deseja percorrer? "))
if pergunta <= 200:
    a = 0.5*pergunta
else:
    a=100+(0.45*(pergunta-200))
print("o preço da passagem é {:.2f}".format(a))
    
                 