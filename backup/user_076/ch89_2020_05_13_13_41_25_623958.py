class Circulo:
    def __init__ (self,centro,raio):
        self.centro = centro
        self.raio = raio
        
    def contem (self,ponto):

        delta_x = ponto.x - self.centro.x
        delta_y = ponto.y - self.centro.y

        d = ((delta_x)**2 + (delta_y)**2)**0.5
        
        if d<=self.raio:
            return True
        else:
            return False
        
        