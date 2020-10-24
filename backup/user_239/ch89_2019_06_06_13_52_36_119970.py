class Circulo():
    def __init__(self,ponto,raio):
        self.raio = raio
        self.pontox = ponto.x
        self.pontoy = ponto.y
    def contem(self,p):
        if (self.pontox - p.x)**2 + (self.pontoy - p.y)**2 >= self.raio**2:
            return True
        else:
            return False
        