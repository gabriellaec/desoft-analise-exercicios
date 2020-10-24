numero=3435
def calcula_munchfksdcsdkcb(numero):
    soma=0
    
    while numero>0:
        num=numero%10 
        soma+=num**num
        numero=int(numero/10)
    return soma 
#print(calcula_munchfksdcsdkcb(numero))      
soma=calcula_munchfksdcsdkcb(numero)
if numero == soma :
    print('True')
else:
    print('False')