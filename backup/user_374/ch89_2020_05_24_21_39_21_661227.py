
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, raio):
        self.centro =  centro
        self.raio = raio
    
    def contem(self, ponto):
        cx = self.centro.x - ponto.x
        cy = self.centro.y - ponto.y
        distancia = (cx**2 + cy**2)**0.5
        if distancia <self.raio:
            return True
        else:
            return False