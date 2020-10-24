class Retangulo:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
    def calcula_perimetro(self):
		return (p1.x - p2.x)*2 + (p1.y-p2.y)*2
    def calcula_area(self):
        return (p1.x - p2.x)*(p1.y-p2.y)
