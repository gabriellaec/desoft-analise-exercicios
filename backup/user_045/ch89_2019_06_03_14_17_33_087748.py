class Circulo:
    def __init__(self):
        self.centro=0
        self.radius=10
    def contem(self, ponto):
        if ponto.x**2+ponto.y**2<=100:
            return True
        else:
            return False