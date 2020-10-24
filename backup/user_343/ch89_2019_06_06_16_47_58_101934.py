class Circulo:
    def __init__(self, ponto, raio):
        self.x=ponto.x
        self.y=ponto.y
        self.raio=p2
       
    def contem(self, ponto):
        if (self.x-ponto.x)**2+(self.y-ponto.y)**2<=self.raio**2:
            return True
        else:
            return False
        	