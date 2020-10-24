class Circulo:
    def __init__(self,centro,raio):
        self.centro = centro
        self.raio = raio
    def contem(self,ponto):
        if self.centro.distancia(ponto) < self.raio:
            return True
        else:
            return False
