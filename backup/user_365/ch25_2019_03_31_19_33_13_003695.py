dist=int(input("qual é a distancia?"))

def calcula_preco(dist):
    if dist <=200:
        valor=dist*0.5
        return valor
    if dist >200:
        valor=dist*0.45
        return valor
print(calcul_preco(dist))