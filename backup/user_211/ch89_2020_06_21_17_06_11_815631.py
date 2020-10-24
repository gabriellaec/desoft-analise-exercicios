class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist(self,outro_ponto):
        ''' Calcula a distância entre o ponto e outro'''
        return ((self.x-outro_ponto.x)**2+(self.y-outro_ponto.y)**2)**(1/2)


class Circulo:
    def __init__(self,centro,raio):
        self.centro = centro
        self.raio = raio
    def contem(self,ponto):
        if self.centro.dist(ponto) < self.raio:
            return True
        else:
            return False