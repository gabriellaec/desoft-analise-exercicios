    
class Retangulo:
    
    def __init__(self, pt_inferior_esquerdo, pt_superior_direito):
        
        self.width = pt_superior_direito.x - pt_inferior_esquerdo.x
        
        self.height = pt_superior_direito.y - pt_inferior_esquerdo.y
        
    def calcula_perimetro(self):
        
        return 2*self.width + 2*self.height
    
    def calcula_area(self):
        
        return self.width*self.height