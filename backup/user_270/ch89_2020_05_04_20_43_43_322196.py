import math
class Circulo:
    def __init__(self,point,raio):
        self.p = point
        self.r = float(raio)
    def contem(self, ponto):
        cal_dis = math.sqrt((self.p.x - ponto.x)**2 + (self.p.y - ponto.y)**2)
        if cal_dis > self.r:
            return False
        else:
            return True