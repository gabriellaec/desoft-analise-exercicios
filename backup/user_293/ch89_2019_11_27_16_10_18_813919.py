class Circulo():
    def __init__(self,ponto,raio):
        self.x = ponto.x
        self.y = ponto.y
        self.Raio = raio
    
    def contem(self,ponto):
        r  = (self.x - ponto.x)**2 + (self.y - ponto.y)**2
        if r <= self.Raio**2:
            return  True
        else:
            False