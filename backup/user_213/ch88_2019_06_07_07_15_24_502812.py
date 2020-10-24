class Retangulo:
    def __init__(self,P1,P2):
        self.P1x = P1.x
        self.P2x = P2.x
        self.P1y = P1.y
        self.P2y = P2.y
        self.ladoy = (self.P2y - self.P1y)
        self.ladox = (self.P2x - self.P1x)
    def calcula_perimetro(self):
        self.perimetro = (self.ladox)*2 + (self.ladoy)*2
    def calcula_area(self):
        self.area = self.ladox * self.ladoy
        
        