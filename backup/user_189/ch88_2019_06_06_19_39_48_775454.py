import pygame 
class retangulo:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        calcula_perimetro(self)=((self.x)*2)+((self.y)*2)
        calcula_area(self)=(self.x)*(self.y)