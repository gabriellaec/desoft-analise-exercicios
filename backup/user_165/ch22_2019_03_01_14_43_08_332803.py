def ano_b(a):
    if a % 400 == 0:
        return True
    elif a % 100 == 0:
    	return False
	elif a % 4 == 0:
        return True 
    else:
        return False
ano = int(input("Ano?"))
print(ano_b(ano))