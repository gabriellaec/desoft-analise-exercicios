class Retangulo:

    def __init__(self,p1,p2):
        self.a = p1
        self.b = p2

    def calcula_perimetro(self):

        rx=self.a.x - self.b.x
        ry=self.a.y - self.b.y
        return (rx+ry)*2

    def calcula_area(self):
        rx=self.a.x - self.b.x
        ry=self.a.y - self.b.y  
        return rx * ry