def collatz_len(inicial):
    
    atual = inicial
    quantidade = 1
    
    while atual != 1:
        if atual % 2 == 0: atual = atual / 2
        else: atual = 3 * atual + 1
        quantidade += 1
   	
    return quantidade

maior_quantidade = 0
numero_inicial = 0

for i in range(1, 1000):
    quantidade = collatz_len(i)
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        numero_inicial = i

print(numero_inicial)