
valor_inicial=float(input('valor inicial: '))
taxa=float(input('taxa: '))
soma=0
i=0
while i < 24:
            mes=valor_inicial*taxa*i
            print(mes)
            soma+=mes
            i+=1
print(soma)           
           