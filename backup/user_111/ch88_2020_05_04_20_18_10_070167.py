class Retangulo:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
       
    def calcula_perimetro(self):
        perimetro=2*(self.p2.x-self.p1.x)+2*(self.p2.y-self.p1.y)
        return perimetro
        
    def calcula_area(self):
        area = (self.p2.x-self.p1.x)*(self.p2.y-self.p1.y)
        return area