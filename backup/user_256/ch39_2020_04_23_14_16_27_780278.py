numero = int(input("Digite um numero: "))
sequencia = numero
lista = sequencia
while numero < 1000:
    if sequencia %2 ==0:
        sequencia = sequencia/2
        lista+= sequencia
    elif sequencia %2 !=0:
        sequencia = 3*sequencia +1
        lista+= sequencia
return lista
        
    