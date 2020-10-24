class Circulo:
    def __init__(self, center, radius):
        self.c = [center.x, center.y]
        self.r = float(radius)
    def contem(self, ponto):
        dx = ponto.x-self.c[0]
        dy = ponto.y-self.c[1]
        d = ((dx**2) + (dy**2)) ** 0.5
        if d <= self.r:
            return True
        else:
            return False

