km=float(input("Quantos quilômetros você deseja percorrer?: "))
if km<=200:
    print('%.2f' %(0.50*km))
if km>200:
    print('%.2f' %(100+0.45*(km-200)))