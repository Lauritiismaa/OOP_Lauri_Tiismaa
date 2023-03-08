#Lauri Tiismaa IT-21 07.03.2023


import math


class kujund:
    
    
    def __init__(self, nurkadearv, pindala):
        self.nurkadearv = nurkadearv
        self.pindala = pindala
        
        
    #def valjastaandmed(self):
       # print("pindala on:" + str(self.pindala))
        

class ring(kujund):
    
    
    def __init__(self,pindala, raadius):
        super().__init__(nurkadearv, pindala)
        self.raadius = raadius
        
        
    def arvutapindala(self):
        self.pindala = self.raadius * self.raadius * math.pi
        print("Ringi pindala on: " + str(self.pindala))
    
    
class ristkylik(kujund):


    def __init__(self, nurkadearv, pindala, korgus, laius):
        super().__init__(nurkadearv, pindala)
        self.korgus = korgus
        self.laius = laius
        
        
    def arvutapindala(self):
        self.pindala = self.korgus * self.laius
        print("Ristküliku pindala on: " + str(self.pindala))
        
        
ringyks =  ring(0, 3)
ringkaks = ring(0, 5)
ristkylikyks = ristkylik(4, 0, 2, 3)
ristkylikkaks = ristkylik(4, 0, 5, 6)
ringyks.arvutapindala()
ringkaks.arvutapindala()
ristkylikyks.arvutapindala()
ristkylikkaks.arvutapindala()