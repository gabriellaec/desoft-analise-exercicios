class Circulo:
    def __init__(self, ponto_centro, raio):
        self.pc = ponto_centro
        self.r = raio

    def contem(self, ponto_x):
        c1 = self.pc.x - ponto_x.x
        c2 = self.pc.y - ponto_x.y
        h = (c1**2 + c2**2)**(1/2)
        if h > self.r:
            return False
        else:
            return True