class Circulo:
    def __init__(self, centro, raio):
        self.c = [centro.x, centro.y]
        self.r = float(raio)
    contem(self, ponto):
        x = ponto.x - self.c[0]
        y = ponto.y - self.c[1]
        dist = ((x**2) + (y**2))**(1/2)
        if dist <= self.r:
            return True
        else:
            return False
        
        
        