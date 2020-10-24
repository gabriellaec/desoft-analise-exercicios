class Circulo:
    """ Classe que representa um Círculo. """
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
        
    def contem(self, ponto):
        if self.ponto(ponto) < self.raio:
            return True
        else:
            return False