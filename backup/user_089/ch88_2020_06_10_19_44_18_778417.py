class Retangulo:
    def __init__(self,p1,p2):
        self.a = p1
        self.b = p2
    def calcula_perimetro(self):
        p = 2*(self.a.x-self.b.x + self.a.y-self.b.y) 
        return p
    def calcula_area(self)   
        a = (self.a.x-self.b.x * self.a.y-self.b.y) 
        return a