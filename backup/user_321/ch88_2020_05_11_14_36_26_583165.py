class Retangulo:
    def __init__ (self, p1, p2):
        self.Ponto1 = p1
        self.Ponto2 = p2
        
    def calcula_perimetro(self):
        dp = (((p1.x - p2.x)**2) + ((p1.y - p2.y)**2)) ** 0.5
        perimetro = ((dp**2)*2)**0.5
        return perimetro
    
    def calcula_area(self):