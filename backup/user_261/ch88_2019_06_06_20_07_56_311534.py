class Retangulo:
    def __init__(self,e,d):
        self.ladog=abs(e.x-d.x)
        self.ladop=abs(d.y-e.y)	
        
    def calcula_perimetro(self):
        pe=2*self.ladog+2*self.ladop
    def calcaula_area(self):
        a=self.ladog*self.ladop
    