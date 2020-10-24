class Circulo:
    def __init__(self, p1, r):
        self.raio = r
        self.x = p1.x
        self.y = p1.y
    def contem(self, ponto):
        if (self.x - ponto.x)**2 + (self.y - ponto.y)**2 <= self.raio**2:
        	return True
        
        else: 
            return False
        