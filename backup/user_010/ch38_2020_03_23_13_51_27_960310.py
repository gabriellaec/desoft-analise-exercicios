numero = str(input("Digite o número:"))
def quantos_uns (x):
    y=0
    i=0
    while i < len(x):
        if x [i] == '1':
            y+=1
            i+=1
        else:
            i+=1
    return y
funcao = quantos_uns (numero)  
print (funcao)