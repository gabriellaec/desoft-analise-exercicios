import math

maior_diferenca = 0

def calcula(a):
    parte1 = 4*a * (180-a)
    parte2 = 40500 - (a*(180-a))
    return parte1/parte2


for ang in range (0, 91, 1):
    angulo = math.radians(ang)
    funcao = math.sin(angulo)
    
    formula= calcula(ang)
    erro = formula-funcao
    
    if abs(erro) > maior_diferenca:
        maior_diferenca = ang
    ang += 1
        
print(maior_diferenca)
    