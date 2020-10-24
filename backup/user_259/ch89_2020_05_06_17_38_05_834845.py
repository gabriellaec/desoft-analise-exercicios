class Circulo:
    def __init__(self,centro,raio):
        self.centro = p1
        self.raio = numero
    
    def Contem(self,ponto):
        if ((self.centro.x-ponto.x)**2+(self.centro.y-ponto.y)**2)**0.5 < self.raio:
            return True
        return False