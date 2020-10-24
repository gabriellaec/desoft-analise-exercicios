class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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