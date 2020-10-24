class retangulo:
    def __init__(self,canto_s,canto_i):
        self.canto_s_x=canto_s.x
        self.canto_s_y=canto_s.y
        self.canto_i_x=canto_i.x
        self.canto_i_y=canto_i.y
    def calc_perimetro(self,canto_s,canto_i):
        lado_x=(self.canto_s_x-self.canto_i_x)*2
        lado_y=(self.canto_s_y-self.canto_i_y)*2
        x=2*lado_x+2*lado_y
        return x
    def calc_area(self):
        lado_x=(self.canto_s_x-self.canto_i_x)
        lado_y=(self.canto_s_y-self.canto_i_y)
        area=lado_x*lado_y
        return area
        
    
    
        