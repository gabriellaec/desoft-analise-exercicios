class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Retangulo:
    def __init__(self, P1, P2):
        self.P1x = P1.x
        self.P1y = P1.y
        self.P2x= P2.x
        self.P2y= P2.y
    def calcula_perimetro(self):
        ladox= self.P2x - self.P1x
        ladoy= self.P2y - self.P1y
        perimetro=2*(ladox)+ 2*(ladoy)
        return perimetro
    def calcula_area(self):
        ladox= self.P2x - self.P1x
        ladoy= self.P2y - self.P1y
        area= ladox*ladoy
        return area
        
    
    