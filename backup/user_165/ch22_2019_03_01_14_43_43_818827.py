def ano_b(a):
    if a % 400 == 0:
        return True
    elif a % 100 == 0:
    	return False
	elif a % 4 == 0:
        return True 
    else:
        return False
print(ano_b(2000))
print(ano_b(2100))
print(ano_b(2400))
print(ano_b(2004))
print(ano_b(2008))