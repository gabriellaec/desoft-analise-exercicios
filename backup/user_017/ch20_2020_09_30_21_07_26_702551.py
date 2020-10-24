x= int(input("Qual a distância que você deseja percorrer em km? "))
if x<200:
    Valor= 0.50*x
else:
    Valor= 0.50*x + 0.45*(200-x)
print(Valor)