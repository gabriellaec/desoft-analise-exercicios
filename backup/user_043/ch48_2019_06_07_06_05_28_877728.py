meses = {'janeiro':1,'fevereiro':2,'março':3,'abril':4,'maio':5,'junho':6,'julho':7,'agosto':8,'setembro':9,'outubro':10,'novembro':11,'dezembro':12}
mes = input('mes: ')

def numero_mes(mes):
    if mes in meses:
        return meses[mes]

numes = numero_mes(mes)

print(numes)
