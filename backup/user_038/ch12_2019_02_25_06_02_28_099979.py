def calcula_area_do_triangulo(base, altura):
    area = base*altura/2
    print("A área do trinagulo é: {0}".format(area))
b = float(input("Informe a base do triângulo: "))
h = float(input("Informe a altura do triângulo: "))
calcula_area_do_triangulo(b,h)