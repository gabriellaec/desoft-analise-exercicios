class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance_to(self, ponto):
    	delta_x = self.x - ponto.x
    	delta_y = self.y - ponto.y
    	return sqrt(delta_x**2 + delta_y**2)

class Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    
    def contem(self, ponto):
        return self.centro.distance_to(ponto) <= self.raio