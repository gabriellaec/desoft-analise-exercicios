class Retangulo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def calcula_perimetro(self):
        return (2*(self.x+self.y))
    def calcula_area(self):
        return (self.x*self.y)