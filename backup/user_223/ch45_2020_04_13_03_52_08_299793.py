numbers=[]
numbers_input=int(input("Insira um número inteiro positivo: "))
numbers.append(numbers_input)
while numbers_input>0:
	numbers_input=int(input("Insira um número inteiro positivo: "))
	numbers.append(numbers_input)
for i in range(len(numbers)-2, -1, -1):
	print (numbers[i])