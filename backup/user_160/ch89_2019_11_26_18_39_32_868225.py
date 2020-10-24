class Circulo ():
    def __init__(self, ponto, raio):
        self.raio = raio
        self.centro = ponto
        
    def contem(self,ponto):
        distancia = (self.centro.x - ponto.x)**2 + (self.centro)
        return distancia < (self.raio)**2

    
    