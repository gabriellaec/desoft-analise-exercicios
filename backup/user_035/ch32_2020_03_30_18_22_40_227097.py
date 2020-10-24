def eh_primo(número):
	div = 3
	if número%2==0 and número!=2 or número==0 or número==1:
		return False
	while número>div:
		if número%div==0:
			return False
		div+=2
	return True
def lista_primo(n):
    