soma = 0 
x = int(input("Digite um número para soma ou 0 para parar de somar:  "))
while x != 0:
    soma += x
    x = int(input("Digite um número para soma ou 0 para parar de somar:  ")) 
print(soma)