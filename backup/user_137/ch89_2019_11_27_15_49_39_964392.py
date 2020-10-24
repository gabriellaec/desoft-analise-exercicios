class Circulo:
    def __init__(self, Pcentro, raio):
        self.Pcentro = Pcentro
        self.raio = raio
        
    def contem(self, ponto):
        if ((ponto.x - self.Pcentro.x)**2 + (ponto.y - self.Pcentro.y)**2)**(1/2) > self.raio:
            return False
        return True