class Retangulo(Ponto):
    def __init__(self,pe,pd):
        self.x1 = pe
        self.y1 = pd
    
    def calculo_perimetro(self):
        x = self.x2 - self.x1
        y = self.y2 - self.y1
        return y*2+x*2
    
    def calcula_area(self):
        x = self.x2 - self.x1
        y = self.y2 - self.y1
        return x*y