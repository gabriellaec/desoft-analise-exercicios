class Retangulo():
    def  __init__(self, ponto1, ponto2):
        self.x1 = ponto1.x
        self.y1 = ponto1.y
        
        self.x2 = ponto2.x
        self.y2 = ponto2.y
    
    def calcula_perimetro(self):
        perimetro = 2*abs(self.x1 - self.x2) + 2*abs(self.y1 - self.y2)
        return perimetro
    def calcula_area(self):
        area = abs(self.x1 - self.x2)*abs(self.y1 - self.y2)
        return area