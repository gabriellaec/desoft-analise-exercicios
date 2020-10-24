def vida(quant, tempo):
    reducao = (tempo/525960) * quant
    return reducao
quant = int(input("quantos vc fuma por dia?:"))
tempo = int(input("ha quantos anos?:"))
print(vida(quant, tempo))
    