def funcao(a,b):
	quantidade=((a*365*60*1440/10*a*b))
	return quantidade
a=int(input("digite o tempo que você fuma em anos"))
b=int(input("digite quantos por dia"))
print(funcao(a,b))