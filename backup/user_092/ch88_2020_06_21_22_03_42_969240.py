class Retangulo(Ponto):
    def __init__(self,x1,y1,x2,y2)
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
    
    def calculo_perimetro(self):
        x = self.x2 - self.x1
        y = self.y2 - self.y1
        return y*2+x*2
    
    def calcula_area(self):
        x = self.x2 - self.x1
        y = self.y2 - self.y1
        return x*y