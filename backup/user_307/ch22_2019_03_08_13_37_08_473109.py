#Se é divisivel por 100 é falso a naõ ser q seja por 400
#Se é divisivel por 4 e não por 100, verdadeiro

a=1800

def eh_bissexto(a):
	if a%400==0:
		return True
	elif a%4==0 and a%100==0:
		return False
	elif a%4==0:
		return True
	else:
		return False
print(eh_bissexto(a))