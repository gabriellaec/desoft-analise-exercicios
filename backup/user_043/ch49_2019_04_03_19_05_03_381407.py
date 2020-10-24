numeros = int(input("Numeros inteiros positivos: "))
listanum = []
              
while numeros>0:
	listanum.append(numeros)
	numeros = int(input("Numeros inteiros positivos: "))
                  
print(listanum[::-1])