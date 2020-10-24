class Circulo:
    def __init__(self, ponto, raio):
        self.ponto = ponto
        self.raio = raio
    def contem(self, ponto2):
        self.dx = self.ponto2.x - self.ponto.x
        self.dy = self.ponto2.y - self.ponto.y
        d = ((self.dx**2)+(self.dy**2))**0.5
        if d <= self.raio:
            return True
        else:
            return False
        






























        
        
    