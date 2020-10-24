meses = True
número = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
número[0] = "Janeiro"
número[1] = "Fevereiro"
número[2] = "Março"
número[3] = "Abril"
número[4] = "Maio"
número[5] = "Junho"
número[6] = "Julho"
número[7] = "Agosto"
número[8] = "Setembro"
número[9] = "Outubro"
número[10] = "Novembro"
número[11] = "Dezembro"
while meses:
	mês = input("Diga um mês")
	if mês==número:
		meses = False
print(número[mês-1])
