class Retangulo:
    def __init__(self,pontox,pontoy,PONTOX,PONTOY):
        x1=pontox
        y1=pontoy
        x2=PONTOX
        y2=PONTOY
        
    def calcula_perimetro(self):
        return (x1-x2)*2+(y1-y2)*2     
    def calcula_area(self):
        return (x1-x2)*(y1-y2)     