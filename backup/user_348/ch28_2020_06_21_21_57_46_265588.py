#usando for
numero = 0

for contador in range (100):
    numero = numero + (1/2**contador)
print(numero)

#usando while
#define um valor inicial para a varivável do exponente
contador = 0
#define um valor inicial para a variável que armazena a soma
numero = 0

#define a codição do loop (enquanto o expoente é menor que 99)
while contador < 99:
    # atualiza o valor da soma
    numero = numero + (1/2**contador)
    # atualiza o valor do expoente
    contador = contador + 1
# imprime a soma quando acaba o loop
print(numero)