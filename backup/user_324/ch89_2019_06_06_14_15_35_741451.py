class Circulo:
    def __init__(self, centro, raio, ponto):
        self.centro=centro
        self.raio=raio
        self.ponto=ponto
    def contem(self, ponto):
        if self.ponto<self.raio:
            return True
        else:
            return False