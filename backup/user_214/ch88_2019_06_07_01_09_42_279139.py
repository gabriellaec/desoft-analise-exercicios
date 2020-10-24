class Retangulo:
    
    def __init__(self, InfEsq, SupDir):
        self.InfEsqx = InfEsq.x
        self.InfEsqy = InfEsq.y
        self.SupDirx = SupDir.x
        self.SupDiry = SupDir.y

    def calcula_perimetro(self):
        Perx = abs(self.InfEsqx-self.SupDirx)
        Pery = abs(self.InfEsqy-self.SupDiry)
        
        Per = 2*Perx + 2*Pery
        
        return Per
    
    def calcula_area(self):
        Perx = abs(self.InfEsqx-self.SupDirx)
        Pery = abs(self.InfEsqy-self.SupDiry)
        
        Area = Perx*Pery
        
        return Area