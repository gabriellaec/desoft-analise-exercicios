def calcula_primos(numero):
    if numero%2==0 and numero!=2: return False
    if numero == 1 or numero == 2: return True
    if numero == 0: return False
    primo=True
    
    for i in range(numero-1,2,-1):
        if numero%i == 0:
            primo = False
            break
    return primo
def verifica_primos(lista):
    i=0
    dicionario={}
    while i<len(lista):
        calculo=calcula_primo(lista[i])
        dicionario[lista[i]]=calculo
	return dicionario
        
    