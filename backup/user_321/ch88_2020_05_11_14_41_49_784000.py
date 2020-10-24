class Retangulo:
    def __init__ (self, Ponto1, Ponto2):
        self.Ponto1 = Ponto1
        self.Ponto2 = Ponto2
        
    def calcula_perimetro(self):
        dp = (((Ponto1.x - Ponto2.x)**2) + ((Ponto1.y - Ponto2.y)**2)) ** 0.5
        perimetro = ((dp**2)*2)**0.5
        return perimetro
    
    def calcula_area(self):
        base = Ponto1.x -Ponto2.x
        h = Ponto1.y - Ponto2.y
        area = base*h
        return area