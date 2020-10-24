class Circulo:
    def __init__(self, c, r):
        self.cx = c.x
        self.cy = c.y
        self.r = r
	def contem(self, ponto):
        if (self.cx - ponto.x)**2 + (self.cy - ponto.y)**2 <= self.r**2:
            return True
        else:
            return False