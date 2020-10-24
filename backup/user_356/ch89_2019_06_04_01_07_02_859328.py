class Circulo():
    def __init__(self, centrox, centroy, raio):
        self.centrox = centrox
        self.centroy = centroy
        self.raio = raio
    def contem(self, ponto):
        if Ponto.x>Circulo.centrox and Ponto.y>Circulo.centroy:
            return "Fora"
        else:
            return "dentro"