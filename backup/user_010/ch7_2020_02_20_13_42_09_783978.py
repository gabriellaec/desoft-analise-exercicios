def calcula_area_do_triangulo(b,h):
    y = b*h/2
    return y
base= int (input(print("Escreva a base do seu retângulo:")))
altura= int (input(print("Escreva a altura do seu retângulo:")))
área= calcula_area_do_triangulo(base,altura)
print ("A área do seu triângulo é {}.".format(área))