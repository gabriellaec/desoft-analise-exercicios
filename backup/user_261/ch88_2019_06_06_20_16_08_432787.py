class Retangulo:
    def __init__(self,e,d):
        self.ladog=abs(e.x-d.x)
        self.ladop=abs(d.y-e.y)	
        
    def calcula_perimetro(self):
        self.pe=(self.ladog*2)+(self.ladop*2)
        return self.pe       
    def calcula_area(self):
        self.a=self.ladog*self.ladop
        return self.a