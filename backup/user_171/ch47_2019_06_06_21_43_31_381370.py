n=input('numero: ')
mes_num={'janeiro':1,'fevereiro':2,'março':3,'abril':4,'maio':5,'junho':6,'julho':7,'agosto':8,'setembro':9,'outubro':10,'novembro': 11,'dezembro':12}
for mes, num in mes_num.items():
    if n==num:
        mes=mes_num[mes]
        print(mes)