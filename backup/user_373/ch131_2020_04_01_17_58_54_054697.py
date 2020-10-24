import random 
dado_1= random.randint (1,10)
dado_2= random.randint (1,10)
soma= dado_1+ dado_2

dinheiro= 10

#fase de dicas

n_jog = int(input( 'Número: '))
print (n_jog )

n2_jog = int(input( 'Outro número >= que o anterior: '))

soma_jog= n_jog + n2_jog

if soma_jog< soma:
    print ('Soma Menor')

elif soma_jog>soma:
    print ('Soma Maior')

else:
    print ( 'Soma no meio')
    
#fase de chutes

print ( 'Fichas disponíveis: ', jogador)

chutes= int(input( 'Adquirir quantos chutes? '))
dinheiro= dinheiro - chutes
resposta= int(input( 'Quanto é a soma? '))

while chute>0 :
    resposta= int(input( 'Quanto é a soma? '))
    if reposta != soma:
        chute=chute -1
    else: 
        dinheiros_total= dinheiro *5
if chute==0:
    dinheiro_total= dinheiro
    print ('Saldo final: ', dinheiro)
        
        