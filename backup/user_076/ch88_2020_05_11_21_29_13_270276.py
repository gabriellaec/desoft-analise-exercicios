class Retangulo:
    def __init__ (self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    def calcula_perimetro (self):
        P = 2*(abs(self.p1.x-self.p2.x)+abs(self.p1.y-self.p2.y))
    def calcula_area (self):
        A = abs(self.p1.x-self.p2.x) * abs(self.p1.x-self.p2.x)