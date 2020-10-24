class Retangulo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def calcula_perimetro(self):
        return 2*(self.p1 + self.p2)
    
    def calcula_area(self):
        return self.p1 * self.p2