def vida(quant, tempo):
    reducao = (quant * 365) * tempo /1 144
    return reducao
 
quant = int(input("quantos vc fuma por dia?:"))
tempo = int(input("ha quantos anos?:"))
print(vida(quant, tempo))
    