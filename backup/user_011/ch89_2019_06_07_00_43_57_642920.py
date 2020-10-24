class Circulo(Ponto):
    def __init__(self,raio):
        self.x = 2
        self.y = 3
        self.centro = (self.x, self.y)
        self.raio = raio
        
RAIO = 15
circulo1  = Circulo(RAIO)