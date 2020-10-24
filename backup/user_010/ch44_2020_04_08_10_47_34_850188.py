meses= {"janeiro":1, "fevereiro":2, "março":3, "abril":4, "maio":5, "junho":6, "julho":7, "agosto":8, "setembro":9, "outubro":10, "novembro":11, "dezembro":12}
mes=input("Digite o mês: ")
x=mes.lower()
if x in meses:
    print ("{0} é o {1}º mês.".format (mes, meses[x]))
else:
    print ("Digite um mês válido.")