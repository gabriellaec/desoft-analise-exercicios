class Circulo:
    def __init__(self,centro,raio):
        self.centro = centro
        self.centro.x = centro.x
        self.centro.y = centro.y
        self.raio = float(raio)
    def contem(self,ponto):
        difx= self.centro.x - ponto.x
        dify= self.centro.y - ponto.y
        dis = (difx**2 + dify**2)**0.5
        if dis<self.raio:
            return True
        else: 
            return False
        