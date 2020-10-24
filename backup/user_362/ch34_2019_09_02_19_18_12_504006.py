meses=1
v0=int(input("Digite o valor de depósito inicial: ") 
juros=float(input("Digite a quantidade de juros: ") 
vf=v0            
while meses<=24:
	vf=vf*(1+juros)
    print('{0:.2f}'.format(prod))
    meses+=1
print('{:.2f}'.format(vf-v0))
            