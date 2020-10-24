class Retangulo ():
	def __init__(self,ponto1,ponto2):
        self.ponto1_x = ponto1.x
    	self.ponto1_y = ponto1.y
        self.ponto2_x = ponto2.x
    	self.ponto2_y = ponto2.y
        self.lado_x = abs(ponto2.x - ponto1.x)
        self.lado_y = abs(ponto2.y - ponto1.y)
	def calcula_perimetro(self):
        return (self.lado_x)*2 + (self.lado_y)*2
    def calcula_area(self):
        return (self.lado_x)*(self.lado_y)
        
    