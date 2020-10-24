def funcao(a,b):
	quantidade=((a*b)*365*1440/10)
	return quantidade
a=int(input("digite o tempo que você fuma em anos"))
b=int(input("digite quantos por dia"))
print(funcao(a,b))