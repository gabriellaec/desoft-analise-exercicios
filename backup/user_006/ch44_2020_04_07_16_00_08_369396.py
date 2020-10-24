mes=input("Digite o nome de um mes:")
meses={"janeiro":1, "fevereiro":2, "março":3, "abril":4, "maio" :5, "junho":6, "julho":7, "agosto":8, "setembro":9, "outubro":10, "novembro":11, "dezembro":12}

if mes in meses:
    n=meses[mes]
    print(n)

#i=0
#while i<len(meses):
#    if mes==meses[i]:
#       print(i+1)
#    i=i+1