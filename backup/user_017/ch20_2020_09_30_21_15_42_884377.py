x= int(input("Qual a distância que você deseja percorrer em km? "))
if x<20:
    Valor= 0.50*x
else:
    Valor= 0.50*200 + 0.45*(x-200)
print(Valor)
