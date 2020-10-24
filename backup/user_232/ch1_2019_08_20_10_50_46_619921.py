def calcula_valor_devido(valor, meses, tx):
    tx = tx/100
    return valor*(1+tx)**meses

x = float(input('valor '))
y = float(input('meses '))
z = float(input('tx '))
vp = calcula_valor_devido(x, y, z)

print(vp)