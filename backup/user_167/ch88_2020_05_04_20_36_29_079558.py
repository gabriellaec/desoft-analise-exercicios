class Retangulo:
    def __init__ (self,a,b):
        self.inferior=a
        self.superior=b
        
    def calcula_perimetro(self):
        ladoX=(self.superior.x-self.inferior.x)*2
        ladoY=(self.superior.y-self.inferior.y)*2
        return(ladoX+ladoY)

    def calcula_area(self):
        area=(self.superior.x-self.inferior.x)*(self.superior.y-self.inferior.y)
        return area
        
  
        
        
   
        
    