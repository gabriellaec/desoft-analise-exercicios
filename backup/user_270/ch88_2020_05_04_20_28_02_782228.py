class Retangulo:
    def __init__(self,Pie,Psd):
        self.p1 = Pie
        self.p2 = Psd
    def calcula_perimetro(self):
        a = self.p2.y - self.p1.y
        b = self.p2.x - self.p2.x
        return 2*(a+b)
    def calcula_area(self):
        a = self.p2.y - self.p1.y
        b = self.p2.x - self.p2.x
        return a*b