numero=3435
def verifica_numero(numero):
    soma=0
    
    while numero>0:
        num=numero%10 
        soma+=num**num
        numero=int(numero/10)
    return soma 
#print(verifica_numero(numero))      
soma=verifica_numero(numero)
if numero == soma :
    print('True')
else:
    print('False')