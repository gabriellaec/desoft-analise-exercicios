
class Circulo:
    def __init__(self, centro, raio, ponto):
        self.centrox= centro.x
        self.centroy= centro.y 
        self.pontox= ponto.x 
        self.pontoy= ponto.y
        self.X= abs(ponto.x-centro.x)
        self.Y= abs(ponto.y-centro.y)
        
    def contem(self):
        H= (self.X**2 + self.Y**2)**(1/2)
        if H <=raio:
        	return True   
        else:
            return False