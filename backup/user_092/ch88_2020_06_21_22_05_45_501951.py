class Retangulo:
    def __init__(self,xe,ye,xd,yd):
        self.x1 = xe
        self.y1 = ye
        self.x2 = xd
        self.y2 = yd
    
    def calculo_perimetro(self):
        x = self.x2 - self.x1
        y = self.y2 - self.y1
        return y*2+x*2
    
    def calcula_area(self):
        x = self.x2 - self.x1
        y = self.y2 - self.y1
        return x*y