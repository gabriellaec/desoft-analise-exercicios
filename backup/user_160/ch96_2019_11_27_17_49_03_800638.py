class Quadrado ():
	def __init__(self, ponto1, ponto2):
        self.ponto1_x = ponto1.x
    	self.ponto1_y = ponto1.y
        self.ponto2_x = ponto2.x
    	self.ponto2_y = ponto2.y
        self.lado_x = abs(10)
        self.lado_y = abs(10)
        
	def calcula_perimetro(self):
        return (self.lado_x) * 2 + (self.lado_y) * 2
    def movePara(self, ponto1,ponto2):
  		self.lado+1 = ponto1
        self.lado+1 = ponto2