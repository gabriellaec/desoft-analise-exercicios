import math
class Circulo:
    def __init__(self, pc, r):
        self.pc=pc
        self.r=float(r)
    def contem(self, p):
        self.p=p
        distancia = ((self.pc.x-self.p.x)**2 +(self.pc.y - self.p.y)**2)**0.5
        if distancia < self.r:
            return True
        else:
            return False