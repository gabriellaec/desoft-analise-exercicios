class Circulo:
    def __init__(self,ponto,raio):
        self.centro.x = ponto.x
        self.centro.y = ponto.y
        self.raio=float(raio)
    def contem(self,ponto):
        difx= self.centro.x - ponto.x
        dify= self.centro.y - ponto.y
        dis= (difx**2 + dify**2)**0.5
        if raio>=dis:
            return True
        else:
            return False
        