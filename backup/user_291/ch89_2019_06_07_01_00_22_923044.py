class Circulo:
    def __init__(self, ponto1, raio):
        self.ponto1x = ponto1.x
        self.ponto1y = ponto1.y
        self.raio = float(raio)
    def contem(self, ponto):
        self.pontox = ponto.x
        self.pontoy = ponto.y
        pitágoras = ((self.ponto1x - self.pontox)**2)+((self.ponto1y - self.pontoy)**2)
        if pitágoras < self.raio**2:
            return True
        else:
            return False