class Retangulo:
    def __init__ (self, Ponto1, Ponto2):
        self.Ponto1 = Ponto1
        self.Ponto2 = Ponto2
        
    def calcula_perimetro(self):
        dp = (((p1.x - p2.x)**2) + ((p1.y - p2.y)**2)) ** 0.5
        perimetro = ((dp**2)*2)**0.5
        return perimetro
    
    def calcula_area(self):
        base = p1.x -p2.x
        h = p1.y - p2.y
        area = base*h
        return area