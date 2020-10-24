lista=[]
valendo=True
i=0
g=0
while valendo:
	palavra=input("Digite uma palavra:")
	primeira_letra= palavra[0]
	if primeira_letra=='a':
		lista[i]=palavra
		i=i+1
	elif palavra=="fim":
		while g<len(lista):
			print(lista[i])
			valendo=False
	else:
		valendo=True