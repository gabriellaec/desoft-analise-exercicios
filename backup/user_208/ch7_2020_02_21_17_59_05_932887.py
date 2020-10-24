def calcula_area_do_triangulo (b,h):
    area_do_triangulo= b*h/2
    return area_do_triangulo

h= int(input(print("Dê a altura do triângulo:")))
b= int(input(print("Dê a base do triângulo:")))
area_do_triangulo=calcula_area_do_triangulo (b,h)
print ("A área do triângulo de base {0} e altura {1} é {2}!!".format(b,h,area_do_triangulo))
