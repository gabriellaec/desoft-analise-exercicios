class Circulo:
    def __init__(self, ponto, raio):
        self.centro = ponto
        self.r = raio

    def contem(self, outro_ponto):
        
        if (outro_ponto.x - self.centro.x)**2 + (outro_ponto.y - self.centro.y)**2 <= (self.r)**2:
            return True
        else:
            return False
        
         

        
   
        