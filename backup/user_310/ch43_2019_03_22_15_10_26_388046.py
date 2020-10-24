numero= 1000

def tamanho_sequencia(n):
    atual=n
    tamanho=0
    while atual>1:
        if atual%2==0:
            tamanho+=1
            atual=atual/2
        
        else:
            tamanho+=1
            atual=3*atual+1
        
    return tamanho+1


maior_sequencia=0
numero_maior_sequencia=0

i=numero

while i>0:
    numero_teste=tamanho_sequencia(i)
    if numero_teste> maior_sequencia:
        maior_sequencia=numero_teste
        numero_maior_sequencia=i
    i-=1
    
print(numero_maior_sequencia)