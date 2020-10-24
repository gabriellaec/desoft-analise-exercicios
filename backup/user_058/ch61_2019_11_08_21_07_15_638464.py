def eh_palindromo(string):
	fraseinvertida=[]
	index = len(string)
	while index > 0: 
		fraseinvertida += string[ index - 1 ]
		index = index - 1
	if fraseinvertida == list(string):
		return True
	else:
		return False
        