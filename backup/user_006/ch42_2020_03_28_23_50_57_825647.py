lista=[]
valendo=True
i=0
g=0
while valendo:
	palavra=input("Digite uma palavra:")
	primeira_letra= palavra[0]
	if primeira_letra=='a':
		palavra=lista[i]
		i=i+1
		valendo=True
	elif palavra=="fim":
		while g<len(lista):
			print(lista[g])
			g=g+1
		valendo=False
	else:
		valendo=True