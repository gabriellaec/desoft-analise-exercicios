class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Circulo:
    central = Ponto()
    raio = 0
    def __init__(self, centro, rail):
        self.central = centro
        self.raio = rail
    def contem_1_2_quadrante (self,ponto):
        if ponto.x < self.central.x + self.raio:
            
    
    