ponto = Ponto(2,4)
centro = Ponto(3,1)
class Circulo:
    def __init__(self, centro, raio, ponto):
        self.centrox= ponto.x
        self.centroy= ponto.y
        self.pontox= centro.x
        self.pontoy= centro.y 
        self.S= abs(ponto.x-centro.x)
        self.H= abs(ponto.y-centro.y)
        
    def contem(self, ponto):
        if (S**2 + H**2)**(1/2)<=raio:
        	return True   
        else:
            return False