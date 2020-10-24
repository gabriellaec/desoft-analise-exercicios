def sequencia_collatz(n):
    contador =- 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = (3*n) + 1
        contador += 1
	return contador

numero = 1000
maior = 0
while numero > 0:
    teste = sequencia_collatz(numero)
    if teste > maior:
        maior = teste
        resultado = numero
	numero -= 1
print(resultado)