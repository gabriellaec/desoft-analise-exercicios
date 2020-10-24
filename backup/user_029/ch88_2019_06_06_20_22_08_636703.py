class Retangulo():
    def __init__(self,ie,sd):
        self.b = (sd.x-ie.x)
        self.h = (sd.y-ie.y)
    def A(self):
        A = self.b*self.h
        return A
    def P(self):
        P = 2*self.b + 2*self.h
        return P
