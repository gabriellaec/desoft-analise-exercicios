def eh_primo(número):
	div = 3
	if número%2==0 and número!=2 or número==0:
		return False
	while número>div:
		if num%div==0:
			return False
		div+=2
	return True