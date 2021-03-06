class Circulo:
    def __init__(self, ponto, raio):
        self.centroX = ponto.x
        self.centroY = ponto.y
        self.raio = raio
    
    def contem(self, ponto):
        dx = self.centroX - self.x
        dy = self.centroY - self.y
        d = ((dx**2) + (dy**2)) ** 0.5
        if d < self.raio:
            return True
        else:
            return False
        