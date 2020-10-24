def preço(km):
    if km<=200:
        return 0.50*km
    if km>200:
        return 100+0.45*(km-200)
        

a=round(float(input("Quantos quilômetros você deseja percorrer?: ")), 2)
z=preço(a)
print(z)