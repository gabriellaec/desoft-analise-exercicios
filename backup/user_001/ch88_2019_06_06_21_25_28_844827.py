
class Retangulo:
    
    def __init__(self,ponto1,ponto2):
        
        self.lengh = math.fabs(ponto1.x) - math.fabs(ponto2.x)
        
        self.height = math.fabs(ponto1.y) - math.fabs(ponto2.y)
        
    def calcula_perimetro(self):
        
        return self.lengh*2 + self.height*2
    
    def calcula_area(self):
        
        return self.lengh*self.height