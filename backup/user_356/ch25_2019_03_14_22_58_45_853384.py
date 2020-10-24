def preço(km):
    if km<=200:
        return 0.5*km
    if km>200:
        return 100+0.45*(km-200)
        

a=int(input("Quantos quilômetros você deseja percorrer?: "))

z=preço(a)

print(z)