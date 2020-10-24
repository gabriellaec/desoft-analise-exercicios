func = input("Está funcionando? Responda sim (s) ou não (n): ")
if func == "s":
	print ("Sem problemas!")
	break
elif func == "n":
	corr = input("Você sabe corrigir? Responda sim (s) ou não (n): ")
	if corr == "s":
		print ("Sem problemas!")
		break
	elif corr == "n":
		prec = input("Você precisa corrigir? Responda sim (s) ou não (n): ")
		if prec == "s":
			print ("Apague tudo e tente novamente")
			break
		elif prec == "n":
			print ("Sem problemas!")
			break
		else:
			print ("Você não respondeu nem s nem n!")
			break
	else:
		print ("Você não respondeu nem s nem n!")
		break
else:
	print ("Você não respondeu nem s nem n!")
	break