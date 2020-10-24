import math

maior_diferenca = 0

def calcula(a):
    parte1 = 4*a * (180-a)
    parte2 = 40500 - (a*(180-a))
    return parte1/parte2


for ang in range (0, 91):
    
    funcao = math.sin(math.radians(ang) 
    
    formula= calcula(ang)
    erro = formula-funcao
    
    if abs(erro) > maior_diferenca:
        maior_diferenca = abs(erro)
        
print(maior_diferenca)
    