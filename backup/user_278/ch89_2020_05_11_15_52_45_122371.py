class Circulo:
    def __init__ (self, centro, raio):
        self.c = centro
        self.r = float (raio)
    def contem (self, ponto):
        dx = self.ponto.x - self.c.x
        dy = self.ponto.y - self.c.y
        if (dx < raio) and (dy < raio):
            True