import math

def check_dimensao():
   dimensao = raw_input("2D ou 3D?
")
   if dimensao == "3D" or dimensao == "3d":
       return "3D"
   elif dimensao == "2D" or dimensao == "2d":
       return "2D"
   else:
       print("Introduza uma resposta valida.")


def introduzir_valores():
   if dimensao == "3D":
       x, y, z = [int(i) for i in raw_input("Introduza as coordenadas separadas por espacos.").split(" ")]
       global x = x
       global y = y
       global z = z
   else:
       x, y = [int(i) for i in raw_input("Introduza as coordenadas separadas por espacos.").split(" ")]
       global x = x
       global y = y
def calcular_norma2D():
   soma_dos_quadrados=coordenadas[0]**2 + coordenadas[1]**2
   norma = math.sqrt(soma_dos_quadrados)
   return norma

def calcular_norma3D():
   soma_dos_quadrados=x**2 + y**2 + z**2
   norma = math.sqrt(soma_dos_quadrados)
   return norma

def calculo():
   if dimensao == "3D":
       print(calcular_norma3D())
   else:
       print(calcular_norma2D())



