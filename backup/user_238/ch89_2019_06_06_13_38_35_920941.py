class Circulo:
    def __init__(self,centro,raio):
        self.x=centro.x
        self.y=centro.y
        self.raio=raio
        
        def contem(self,ponto):
			xp=ponto.x
            yp=ponto.y
            if (self.x-xp)**2+(self.y-yp)**2 <= self.raio**2:
                return True
            else:
                return False