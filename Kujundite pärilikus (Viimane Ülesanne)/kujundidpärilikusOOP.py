#Lauri Tiismaa IT-21 1.03.2023
import math


class kujund:
    
    
    def pindala(self):
        pass


class ruut(kujund):
    
    
    def __init__(self, kuljepikkus):
        self.kuljepikkus = kuljepikkus
    

    def pindala(self):
        return self.kuljepikkus * self.kuljepikkus
    

class ring(kujund):
    
    
    def __init__(self, raadius):
        self.raadius = raadius
        
        
    def pindala(self):
        return self.raadius * self.raadius * math.pi
      
        
kujund1 = ruut(3)
kujund2 = ring(5)

print("Ruudu pindala on: ", kujund1.pindala())
print("ringi pindala on: ", kujund2.pindala())
