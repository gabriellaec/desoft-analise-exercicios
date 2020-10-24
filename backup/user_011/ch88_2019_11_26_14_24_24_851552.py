class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Retangulo:
    
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2
        
   	def calcula_perimetro(self):
        
        lado1 = abs(self.ponto1.x - self.ponto2.x)
        lado2 = abs(self.ponto1.y - self.ponto2.y)
        
        return lado1*2 + lado2*2
    def calcula_area(self):
        
        lado1 = abs(self.ponto1.x - self.ponto2.x)
        lado2 = abs(self.ponto1.y - self.ponto2.y)
        
        return lado1*lado2