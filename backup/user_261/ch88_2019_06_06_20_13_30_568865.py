class Retangulo:
    def __init__(self,e,d):
        self.ladog=abs(e.x-d.x)
        self.ladop=abs(d.y-e.y)	
        
    def calcula_perimetro(self):
        pe=(ladog*2)+(ladop*2)
        return(pe)                  
    def calcaula_area(self):
        a=self.ladog*self.ladop
    	return(a)