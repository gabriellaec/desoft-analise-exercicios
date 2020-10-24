class Retangulo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def calcula_perimetro(self):
        perimetro = 2*(x+y)
        return perimetro
        
        
    def calcula_area(self):
        area = x * y
        return area


# Programa Principal    
p1 = Retangulo(5,4)
p2 = Retangulo(3,2)
    
perim = p1.calcula_perimetro(10,4)
area = p1.calcula_area(5,2)
    
print('perim:{0},area:{1}'.format(perim,area))