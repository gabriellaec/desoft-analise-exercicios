class Circulo:
    def __init__(self,ponto,raio):
        self.x = ponto.x
        self.y = ponto.y
        self.raio=float(raio)
    def contem(self,ponto):
        difx= self.x - ponto.x
        dify= self.y - ponto.y
        dis= (difx**2 + dify**2)**0.5
        if raio>=dis:
            return True
        else:
            return False
        