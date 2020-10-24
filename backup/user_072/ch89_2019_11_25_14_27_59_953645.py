
class Circulo:
    def __init__(self, centro, raio, ponto):
        self.centrox= centro.x
        self.centroy= centro.y 
        self.pontox= ponto.x 
        self.pontoy= ponto.y
        self.S= abs(ponto.x-centro.x)
        self.H= abs(ponto.y-centro.y)
        
    def contem(self, ponto):
        if (self.S**2 + self.H**2)**(1/2)<=raio:
        	return True   
        else:
            return False