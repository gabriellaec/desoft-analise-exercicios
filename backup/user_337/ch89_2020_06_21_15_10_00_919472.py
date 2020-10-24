class Circulo:
    def __init__(self, centro, raio):
        self.x = centro.x
        self.y = centro.y
        self.raio = raio
    def contem(self, ponto):
        distancia = sqrt((self.x-ponto.x)**2 +(self.y-ponto.y)**2)
        if distancia <= self.raio:
            return 'dentro'
        else:
            return'fora'