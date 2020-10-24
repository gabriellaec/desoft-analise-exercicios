class ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, other_point):
    """ Calcula a distância entre o próprio ponto e o outro ponto."""
        return sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

class Circulo:
    """ Classe que representa um Círculo. """
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    def contem(self, ponto):
        if self.centro.distance_to(ponto) < self.raio:
            return True
        else:
            return False