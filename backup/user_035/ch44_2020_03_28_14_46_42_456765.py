meses = True
while meses:
	Tempo = [1,2,3,4,5,6,7,8,9,10,11,12]
	mês = input("Diga um mês")
	if mês=="Janeiro":
		meses = False
	elif mês=="Fevereiro":
		meses = False
	elif mês=="Março":
		meses = False
	elif mês=="Abril":
		meses = False
	elif mês=="Maio":
		meses = False
	elif mês=="Junho":
		meses = False
	elif mês=="Julho":
		meses = False
	elif mês=="Agosto":
		meses = False
	elif mês=="Setembro":
		meses = False
	elif mês=="Outubro":
		meses = False
	elif mês=="Novembro":
		meses = False
	else:
		meses = False
print(Tempo[mês-1])
