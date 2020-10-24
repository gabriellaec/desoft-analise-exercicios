class Circulo:
    def __init__(self,centro,raio):
        self.centro=centro
        self.raio=raio
    def contem(self,ponto):
        if ponto.x<=self.centro.x+self.raio and ponto.x>=self.centro.x-self.raio and ponto.y<=self.centro.y+self.raio and ponto.y>=self.centro.y-self.raio:
            return True
        else:
            return False
        