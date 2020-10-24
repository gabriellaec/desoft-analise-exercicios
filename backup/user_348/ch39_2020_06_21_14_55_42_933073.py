termos = 1
maior_sequencia = 0
numero_com_maior_sequencia = 0
for n in range(1, 1000):
    if (n% 2 ==0):
        numero = n/s
    else:
        numero = 3 * n + 1
        
while numero != 1:
    if (numero % 2 ==0):
        numero = numero/2
    else:
        numero = 3*numero + 1
    termos = termos + 1
    if termos > maior_sequencia:
        maior_sequencia = termos
        numero_com_maior_sequencia = numero

print(numero_com_maior_sequencia)
    
        
    
    