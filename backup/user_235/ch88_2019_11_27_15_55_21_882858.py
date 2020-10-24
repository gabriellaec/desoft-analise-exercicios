class Rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def calcula_perimetro(self,b,h):
        perimetro = 2*(b+h)
        return perimetro
        
        
    def calcula_area(self,b,h):
        area = b * h
        return area


# Programa Principal    
p1 = Rectangle(5,4)
p2 = Rectangle(3,2)
    
perim = p1.calcula_perimetro(10,4)
area = p1.calcula_area(5,2)
    
print('perim:{0},area:{1}'.format(perim,area))