'''Esta função serve para verificar se um número é ou não um quadrado perfeito utilizando o método
de subtrair numeros primos ímpares do número desejado.
Caso ao subtrair os numeros primos impares do numero desejado e o resultado for zero, ele é um quadrado
perfeito, caso contrário, ele não é
'''
def verifica_quadrado_perfeito(x):
    lista_menos = []
    lista_menos.append(1)
    i = 0
    while x > 0:
        impar_menos = lista_menos[i] + 2
        lista_menos.append(impar_menos)
        x -= lista_menos[i]
        i += 1
        if x == 0:
            return True
        elif x < 0:
            return False
    