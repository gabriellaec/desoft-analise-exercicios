class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
centro=(0,0)
raio=5
ponto(6,6)
class Circulo:
    def __init__(self, centro, raio):
        self.centrox=centro.x
        self.centroy=centro.y
        self.raio=raio
   	def contem(self, ponto):
        self.pontox=ponto.x
        self.pontoy=ponto.y
        if r**2>(self.centrox-self.pontox)**2+(self.centroy-self.pontoy)**2:
            return False
        else:
            return True
        
