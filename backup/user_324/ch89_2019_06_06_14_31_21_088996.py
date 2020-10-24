class Circulo:
    def __init__(self, centro, raio):
        self.centrox=centro.x
        self.centroy=centro.y
        self.raio=raio
    def contem(self, ponto):
        self.pontox=ponto.x
        self.pontoy=ponto.y
        if raio**2>(self.centrox-self.pontox)**2+(self.centroy-self.pontoy)**2:
            return False
        else:
            return True
        
