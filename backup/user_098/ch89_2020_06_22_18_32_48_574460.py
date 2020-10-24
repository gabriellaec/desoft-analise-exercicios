class Circulo:
  def __init__(self,centro,raio):
        self.x = centro[0]
        self.y = centro[1]
        self.raio = raio

  def contem(self, ponto):
    dx = ponto.x - self.x
    dy = ponto.y - self.y
    if ((dx**2) + (dy**2)) ** 0.5 < self.raio:
        return True
    else:
        return False