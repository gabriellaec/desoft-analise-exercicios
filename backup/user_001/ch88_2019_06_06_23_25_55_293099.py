
class Retangulo:
    
    def __init__(self,ponto1,ponto2):
        
        self.lengh = (ponto1.x**2)**0.5 - (ponto2.x**2)**0.5
        
        self.height = (ponto1.y**2)**0.5 - (ponto2.y**2)**0.5
        
    def calcula_perimetro(self):
        
        return self.lengh*2 + self.height*2
    
    def calcula_area(self):
        
        return self.lengh*self.height