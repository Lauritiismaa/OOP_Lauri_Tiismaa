#Lauri Tiismaa IT-21 22.02.2023


class loomad:
    
    
    def __init__(self, haalitsus):
        self.haalitsus = haalitsus
        #print(haalitsus)
    
    
class koer(loomad):
    
    
    def __init__(self, haalitsus):
        super().__init__(haalitsus)
        print("Koer:", self.haalitsus)
        
    
class kass(loomad):
    
    
    def __init__(self, haalitsus):
        super().__init__(haalitsus)
        print("Kass:", self.haalitsus)
        
        
class hobune(loomad):
    
    
    def __init__(self, haalitsus):
        super().__init__(haalitsus)
        print("hobune:", self.haalitsus)
        
        
class part(loomad):
    
    
    def __init__(self, haalitsus):
        super().__init__(haalitsus)
        print("Part:", self.haalitsus)
        
        
loom1 = koer("woof woof")
loom2 = kass("meow meow")
loom3 = hobune("PRRRR PRRR")
loom4 = part("quak quak")