
valor_inicial=float(input('valor inicial: '))
taxa=float(input('taxa: '))
soma=0
i=1
while i <= 24:
            mes=valor_inicial(1+taxa)**i
 			print('{0:.2f}'.format(mes))
       		i+=1
ganho=mes-valor_inicial
print(ganho)
           