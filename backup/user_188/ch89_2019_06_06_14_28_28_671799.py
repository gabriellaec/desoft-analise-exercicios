classe Circulo:
    def __init__(self, centro, raio):
        self.centro = centro
        self.raio = raio
    def contem(self, ponto):
        distancia_centro_ponto_x = abs(self.centro.x - self.ponto.x)
        distancia_centro_ponto_y = abs(self.centro.y - self.ponto.y)
        distancia_real = (distancia_centro_ponto_x**2 + distancia_centro_ponto_y**2) ** (1/2)
        if distancia_real <= self.raio:
            print("O ponto está contido no círculo")
        else:
            print("O ponto não está contido no círculo")