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

def lista_primos(n):
	lista=[]
	controle=2
	while len(lista)<n:
		if eh_primo(controle)==True:
			lista.append(controle)
		controle+=1
	return lista
    