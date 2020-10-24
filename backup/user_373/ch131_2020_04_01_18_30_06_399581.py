import random 
dado_1= random.randint (1,10)
dado_2= random.randint (1,10)
soma= dado_1+ dado_2

#fase de dicas

n_jog = int(input( 'Número: '))
n2_jog = int(input( 'Outro número >= que o anterior: '))

if n_jog> soma:
    print ('Soma menor')
elif n2_jog < soma:
    print ('Soma maior')
else:
    print ('Soma no meio')
 
dinheiro = 10   
print ('Você tem: ', dinheiro)

chute= int(input('Quantos chutes?  ')
dinheiro -= chute
           
while chute > 0:
           chute= int(input('chute novamente:'))
           if chute != soma:
               chute= chute -1
           else:
               total= dinheiro+ 5*dinheiro
               break
if chute==0:
           total= dinheiro
           print ('total', total)

                      