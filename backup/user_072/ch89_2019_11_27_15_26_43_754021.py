
class Circulo:
    def __init__(self, centro, raio, ponto):
        self.centrox= centro.x
        self.centroy= centro.y 
        self.pontox= ponto.x 
        self.pontoy= ponto.y
        self.X= abs(ponto.x-centro.x)
        self.Y= abs(ponto.y-centro.y)
        
    def contem(self,ponto):
        H= (ponto.x**2 + ponto.y**2)**(1/2)
        if H <=raio:
        	return True   
        else:
            return False