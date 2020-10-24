class Retangulo:
    def __init__(self, p1, p2):
        self.pi=p1
        self.ps=p2
    def calcula_perimetro(self):
        peri=self.ps.x-self.pi.x
        pery=self.ps.y-self.pi.y
        return 2*(peri+pery)
    def calcula_area(self):
        peri=self.ps.x-self.pi.x
        pery=self.ps.y-self.pi.y
        return peri*pery
    
    