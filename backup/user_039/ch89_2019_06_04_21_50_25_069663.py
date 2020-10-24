import math
class Circulo:
    def __init__(self,p1,r):
        self.centro =  p1
        self.raio = float(r)
        
    def contem(self, ponto):
        self.distancia_x = abs(ponto.x - self.centro.x) 
        self.distancia_y = abs(ponto.y - self.centro.y)
        self.distancia_de_c_p1 = math.sqrt(self.distancia_x**2 + self.distancia_y**2)
        return self.distancia_de_c_p1 <= self.raio