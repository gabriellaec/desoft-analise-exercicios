dist=float(input("qual é a distancia?"))

def calcula_preco(dist):
    if dist <=200:
        valor=dist*0.5
        return valor
    if dist >200:
        valor=100+(dist-200)*0.45
        return valor
print('o valor é {:.2f}'.format(calcula_preco(dist)))