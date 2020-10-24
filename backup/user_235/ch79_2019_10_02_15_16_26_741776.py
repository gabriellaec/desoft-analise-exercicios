lista = ['a','b','c','d','e','f','g','h']
indices = ['00','01','02','03','04','05','06','07','08']  
def monta_dicionario(x,y):
    dicionario_montado = {}
    for i in x:
        dicionario_montado[i] = y[x.index(i)]
    return dicionario_montado
print(monta_dicionario(lista,indices))
