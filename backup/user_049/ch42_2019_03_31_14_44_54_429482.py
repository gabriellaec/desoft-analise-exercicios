numero=int(input('Diga um número: '))
numero=str(num)

cont=0
quant=0

def quantos_uns(num):
    
    while cont<len(num):
        
        if num == '1':
            quant+=1
            cont+=1
        else:
            cont+=1
            
print(quant)