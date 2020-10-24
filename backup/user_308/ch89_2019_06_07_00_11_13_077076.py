class Circulo:
    def __init__(self,centro,raio):
        self.cx=centro.x
        self.cy=centro.y
        self.raio=raio
    def contem(self,ponto):
        self.px=ponto.x
        self.py=ponto.y
        distancia_pontos=(((self.px-self.cx)**2)+((self.py-self.cy)**2))**(1/2)
        if distancia_pontos>self.raio:
            dentro=False
        else:
            dentro=True
        return dentro