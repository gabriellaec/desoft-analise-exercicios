class Circulo:
    def __init__(self, Ponto_central, raio):
        self.Pc = Ponto_central
        self.r = raio
    def contem(self, ponto):
        dist = ((self.Pc.x - ponto.x)**2+(self.Pc.y - ponto.y)**2)**0.5
        if dist <= self.r:
            return True
        else:
            return False