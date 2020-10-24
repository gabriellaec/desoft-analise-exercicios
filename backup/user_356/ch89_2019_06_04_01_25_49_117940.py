class Circulo():
    def __init__(self, centrox, centroy, raio):
        self.centrox = centrox
        self.centroy = centroy
        self.raio = raio
    def contem(self, ponto):
        if (Circulo.centrox-Ponto.x)**2 +(Circulo.centroy-Ponto.y)**2>=Circulo.raio**2:
            return "Fora"
        else:
            return "dentro"
        