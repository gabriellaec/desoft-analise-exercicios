class Circulo:
    def __init__(self,centro,raio):
        self.x = centro.x
        self.y = centro.y
        self.raio = float(raio)
    def contem(self,ponto):
        difx= self.x - ponto.x
        dify= self.y - ponto.y
        dis = (difx**2 + dify**2)**0.5
        if dis<raio:
            return True
        else: 
            return False
        