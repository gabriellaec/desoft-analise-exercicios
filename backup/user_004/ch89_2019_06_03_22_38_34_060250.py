class Circulo:
    def centro(self, ponto1):
        self.centro = (ponto1.x, ponto1.y)
        self.raio = 2.5
    
    def contem(self, ponto):
        if ponto.x>ponto1.x+2.5 and ponto.y>ponto1.y+2.5:
            return 'Está fora'
        else:
            return 'Está dentro'