meses = True
while meses:
	número = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	número[0] = "JANEIRO"
	número[1] = "FEVEREIRO"
	número[2] = "MARÇO"
	número[3] = "ABRIL"
	número[4] = "MAIO"
	número[5] = "JUNHO"
	número[6] = "JULHO"
	número[7] = "AGOSTO"
	número[8] = "SETEMBRO"
	número[9] = "OUTUBRO"
	número[10] = "NOVEMBRO"
	número[11] = "DEZEMBRO"
	mês = input("Diga um mês")
	if mês==número:
		meses = False
print(número[mês])
