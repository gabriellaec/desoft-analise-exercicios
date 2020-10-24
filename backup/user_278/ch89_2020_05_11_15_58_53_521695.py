class Point:
    def __init__ (self,vx,vy):
        self.x = vx
        self.y = vy

    def distance_to (self,other_point):
        d = sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
        return d

class Circulo:
    def __init__ (self,pm,r):
        self.centro = pm
        self.raio = r
    
    def dentro (self,ponto):
        if self.centro.distance_to(ponto) < self.raio:
            return True
        else:
            return False