soma = 0
numero = int(input("Digite um número: "))

while numero != 0:
        
    soma += numero
    numero = int(input("Digite um número: "))

if numero == 0:
       print("A soma desses números é {0}".format(soma))