lista = []
numero1 = 1

while numero1 < 1000:
    numero = numero1   # Variável para rodar no próximo while
    numero_de_termos = 1  # Contador
    while numero != 1:
                    
        if numero %2 == 0:
            numero = numero/2
            numero_de_termos += 1
        else:
            numero = 3*numero + 1              
            numero_de_termos += 1

    lista.append(numero_de_termos)
    numero1 += 1



print(max(lista))

j = 0
while lista[j] < max(lista):
    j += 1

print(j)
numero_para_seq_max = j + 1
print(numero_para_seq_max)