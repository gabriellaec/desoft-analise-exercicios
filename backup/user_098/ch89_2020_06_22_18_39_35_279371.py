class Circulo:
  def __init__(self,Ponto,raio):
        self.x = Ponto.x
        self.y = Ponto.y
        self.raio = float(raio)

  def contem(self, ponto):
    dx = ponto.x - self.x
    dy = ponto.y - self.y
    distancia = ((dx**2) + (dy**2)) ** 0.5
    if distancia <= self.raio:
        return True
    else:
        return False