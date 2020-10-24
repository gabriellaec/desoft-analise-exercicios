class Retangulo:
    def __init__(self,infesq,supdir):
        self.infesqx = infesq.x
        self.infesqy = infesq.y
        self.supdirx = supdir.x
        self.supdiry = supdir.y
        
    def calcula_perimetro(self):
        lado1 = self.supdirx - self.infesqx
        lado2 = self.supdiry - self.infesqy
        p = lado1*2 + lado2*2
        return p 
    
    def calcula_area(self):
        lado12 = self.supdirx - self.infesqx
        lado22 = self.supdiry - self.infesqy
        a = lado12*lado22
        return a 
    
    
        
        
       
        
