class Circulo:
    def __init__(self, centro, raio):
        self.x = centro.x
        self.y = centro.y
        self.r = raio
    def contem(self, ponto):
        dx = self.x - ponto.x
        dy = self.y - ponto.y
        D = (dx**2 + dy**2)**0.5
        if D <= self.r:
            return True
        else:
            return False