def eh_primo(numero):
	impar=3
	if numero==0 or numero==1:
		return False
	if numero==2:
		return True
	if numero%2==0:
		return False
	while impar<numero:
		if numero%impar==0:
			return False
		impar+=2
	return True

def primos_entre(a,b):
	p=0
	while a<=b:
		if eh_primo(a)==True:
			p+=1
		a+=1
    return p