class Circulo():
    
    def __init__(self, _centro, _raio):
        self.centro = _centro
        self.raio = _raio 
        
    def contem(self, ponto):
        self.pontinho = ponto
        self.distancia_x = (self.centro.x - self.pontinho.x)
        self.distancia_y = (self.centro.y - self.pontinho.y)
        
        self.distancia = ((self.distancia_x**2) + (self.distancia_y**2))**(1/2)
        
        if self.distancia < self.raio:
            return True 
        else:
            return False