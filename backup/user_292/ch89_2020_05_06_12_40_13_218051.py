class Circulo:
    def __init__(self, centro, raio):
        self.c = centro
    def contem(self, ponto):
        self.z = ponto
        d = ((self.c.x + self.z.x)**2 - (self.c.y - self.z.y)**2)** 0.5
        if d >= raio:
            return "sim"
        else:
            return "nao"