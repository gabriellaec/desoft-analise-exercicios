class Retangulo:
    def __init__(self, Pesq, Pdir):
        self.esq = [Pesq.x, Pesq.y]
        self.dir = [Pdir.x, Pesq.y]
        
    def calcula_perimetro(self):
        p = 2*(self.dir[0] - self.esq[0]) + 2*(self.dir[1] - self.esq[1])
        return p
    
    def calcula_area(self):
        a = (self.dir[0] - self.esq[0])*(self.dir[1] - self.esq[1])
        return a