def eh_primo(numero):
	impar=3
	if numero==0 or numero==1:
		return False 
	if numero==2:
		return True 
	if numero%2==0:
		return False 
	while numero>impar:
		if numero%impar==0:
			return False 
		impar+=2
	return True 
def verifica_primos(listanum): 
	dicionario = {}
	i = 0
	while i < (len(listanum)):
		booleano = eh_primo(listanum[i]) 
		dicionario[listanum[i]] = booleano 
		i = i+1
	return dicionario 
	a = verifica_primos([-1,0,1,2,3,4,5,6,7,8,9])
print (a)