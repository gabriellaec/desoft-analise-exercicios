class Circulo:
    def __init__(self, p1, r):
        self.raio = r
        self.centrox = p1.x
        self.centroy = p1.y
    def contem(self, ponto):
            
        self.x = ponto.x
        self.y = ponto.y
        if self.x <= self.centrox + self.raio and self.x >= self.centrox - self.raio:
            if self.y <= self.centroy + self.raio and self.y >= self.centroy - self.raio:
                return True
        else: 
            return False
        