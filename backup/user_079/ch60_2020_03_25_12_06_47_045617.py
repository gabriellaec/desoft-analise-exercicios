z=str(input('z?:'))
def eh_palindromo(z):
	y=z[::-1]
	if z == y:
		return True   
	else:
		return False