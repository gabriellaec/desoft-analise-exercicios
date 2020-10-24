class Circulo:
    def __init__(self, x, y,raio):
        self.x = x
        self.y = y
        self.raio=raio
    def contem(self, ponto):
        if (self.x-x)**2+(self.y-y)**2<=raio**2:
            return True
        else:
            return False
        