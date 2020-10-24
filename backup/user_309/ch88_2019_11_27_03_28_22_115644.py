class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Retangulo:
    def __init__(self,p1,p2):
        self.p1eqs = p1
        self.p2dir = p2
    
    def calcula_perimetro(self):
        perimetro = lado * 4
        return perimetro
        
        
    def calcula_area(self):
        area = lado * lado
        return area
    