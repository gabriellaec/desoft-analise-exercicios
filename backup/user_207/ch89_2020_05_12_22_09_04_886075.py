class Circulo:
    def __init__(self, ponto_centro, raio):
        self.centro_x = ponto_centro.x
        self.centro_y = ponto_centro.y
        self.raio = raio
        
    def contem(self, ponto):
        dx = ponto.x - self.centro_x
        dy = ponto.y - self.centro_y
        d = (dx**2 + dy**2)**(0.5)
        
        if d< self.raio:
            return True
        else:
            return False