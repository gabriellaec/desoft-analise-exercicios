import math
class Circulo:
    def __init__(self, pc, r):
        self.pc=pc
        self.r=float(r)
    def contem(self, p):
        if self.pc.distance_to(p)< self.r:
            return True
        else:
            return False