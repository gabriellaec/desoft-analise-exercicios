import math
class Circulo:
    def __init__(self,p1,r):
        self.centro =  p1
        self.raio = float(r)
        self.distancia_x = abs(r.x-p1.x) 
        self.distancia_y = abs(r.y-p1.y)
        self.distancia_de_c_p1 = abs(math.sqrt(self.disciancia_x**2+self.distancia_y**2)
        
    def contem(self, ponto):
        return self.distancia_de_c_p1 <= self.raio