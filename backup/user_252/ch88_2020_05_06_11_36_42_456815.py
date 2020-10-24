class Retangulo:
    def __init__(self, p1, p2):
        self.x=p1
        self.y=p2
    def calcula_perimetro(self):
        peri=self.y-self.x
        pery=self.y.y-self.x.y
        return 2*(peri+pery)
    def calcula_area(self):
        peri=self.y.x-self.x.x
        pery=self.y.y-self.x.y
        return peri*pery
    
    