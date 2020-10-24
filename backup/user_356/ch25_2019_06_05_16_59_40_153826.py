km=float(input("Quantos quilômetros você deseja percorrer?: "))
if km<=200:
    return '%.2f' %(0.50*km)
if km>200:
    return '%.2f' %(100+0.45*(km-200))