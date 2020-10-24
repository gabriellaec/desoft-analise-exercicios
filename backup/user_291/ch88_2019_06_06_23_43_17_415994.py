class Retangulo():
    def __init__(self, ponto1, ponto2):
        self.ponto1x = ponto1.x
        self.ponto1y = ponto1.y
        self.ponto2x = ponto2.x
        self.ponto2y = ponto2.y
	def calcula_perimetro(self):
        ladox = (self.ponto1x - self.ponto2x)*2 
        ladoy = (self.ponto2y - sself.ponto1y)*2
        perimetro = ladox + ladoy
        return perimetro
    def calcula_area(self):
        ladox = (self.ponto1x - self.ponto2x)
        ladoy = (self.ponto2y - self.ponto1y)
        Area = ladox*ladoy
        return Area