import math
class Retangulo:
    def __init__(self, ponto_Infesquerdo, ponto_Supdireito):
        
        ponto1 = ponto_Infesquerdo
    	ponto2 = ponto_Supdireito
    
   		self.ladox = math.fabs(ponto1.x - ponto2.x)
   		self.ladoy = math.fabs(ponto1.y - ponto2.y)
        
    def calcula_perimetro(self):
        self.perimetro = 2*self.ladox + 2*self.ladoy
        return self.perimetro
    
   	def calcula_area(self):
        self.area = self.ladox * self.ladoy
        return self.area
    
    