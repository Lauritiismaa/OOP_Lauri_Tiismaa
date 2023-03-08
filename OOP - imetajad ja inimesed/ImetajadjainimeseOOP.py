#Lauri Tiismaa IT-21 28.02.2023

class loomad:
    
    
    def __init__(self, kasonjalad, korgus, toitumine, vanus):
        if kasonjalad == True or kasonjalad == False:
            self.kasonjalad = kasonjalad
        self.korgus = korgus
        if toitumine == "Taime" or toitumine == "Liha" or toitumine == "Sega":
            self.toitumine = toitumine
        self.vanus = vanus
        
        
    def kasva(self, korgus):
        self.korgus = korgus
        print("Uus kõrgus on: ", self.korgus)
        
        
    def vanane(self, vanus):
        self.vanus = vanus
        print("Uus vanus on: ", self.vanus)
        
        
class imetajad(loomad):
    
    
    def __init__(self, kasonjalad, korgus, toitumine, vanus, sugu):
        super().__init__(kasonjalad, korgus, toitumine, vanus)
        if sugu == "M" or sugu == "N":
            self.sugu = sugu
        
        
    def sure(self, vanus):
        if vanus > 211:
            print("Olete surnud!")
            
            
class inimene(imetajad):
    
    
    def __init__(self, kasonjalad, korgus, toitumine, vanus, sugu, nimi, kodakondsus):
        super().__init__(kasonjalad, korgus, toitumine, vanus, sugu)
        self.nimi = nimi
        self.kodakondsus = kodakondsus
        
        
    def sure2(self):
        if self.vanus > 121:
            print("Olete surnud!")
            
            
    def andmed(self):
        print("Tere", self.nimi,", sa oled", self.kodakondsus,".Sa oled", self.vanus,
              "aastat vana ning oled", self.korgus,"cm kõrge. Sa oled", self.sugu,
              "soost ja oled", self.toitumine,"toitlane")
        
        
inimeneyks = inimene("True", 187, "Sega", 17, "M", "Lauri", "Eestlane")
inimeneyks.kasva(190)
inimeneyks.vanane(180)
inimeneyks.sure2()
inimeneyks.andmed()
    