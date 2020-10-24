class Retangulo:
    def __init__(self,p1,p2):
        self.ie=p1
        self.sd=p2
    def calcula_perimetro(self):
        return (2*(self.sd.x-self.ie.x)+(self.sd.y-self.ie.y))
    def calcula_area(self):
        return (self.sd.x-self.ie.x)*(self.sd.y-self.ie.y)