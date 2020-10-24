distancia=int(input("Qual a distancia que deseja percorer? "))
if distancia >= 200:
    preco = distancia*0.5
elif distancia < 200:
    preco = distancia*0.45
    
print("O preço da passagem é {0:.2F}.format(preco))    

    
