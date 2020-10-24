class Circulo:
    def __init__(self, p1, r):
        self.x = p1
        self.y = r
    def distance_to(self, ponto):
        dx = ponto.x - self.x.x
        dy = ponto.y - self.x.y
        return ((dx**2) + (dy**2)) ** 0.5
    def contem(self, ponto):
        if distance_to(self, ponto) < r:
            return True
        else:
            return False