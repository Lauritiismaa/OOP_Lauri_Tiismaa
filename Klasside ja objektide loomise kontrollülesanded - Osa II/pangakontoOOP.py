#Lauri Tiismaa IT-21 22.02.2023
class pangakonto:
    
    def __init__(self, kontoseis, omanikunimi):
        self.kontoseis = kontoseis
        self.omanikunimi = omanikunimi
        
        
    def andmed(self):
        print("Teie pangakonto seis on: ", self.kontoseis, "Omanik on :", self.omanikunimi)
    
    
    def rahalisamine(self, summa):
        if summa > 0:
            self.kontoseis += summa
            #print("Lisasite kontole:", summa "Eurot, Teie kontoseis on: " , self.kontoseis)
        else:
            print("Te ei saa kontole sellist summat lisada")
            
            
    def rahavalja(self, vahe):
        if vahe > 0:
            self.kontoseis -= vahe
            print("Võtsite välja: ", vahe," Eurot, teie kontoseis on: ", self.kontoseis)
        else:
            print("Te ei saa välja võtta rohkem raha kui teil kontol on!!!")
            
            
kontoyks = pangakonto(1500, "Peeter")
kontokaks = pangakonto(2000, "Madis")
kontoyks.andmed()
kontokaks.andmed()
kontoyks.rahalisamine(700)
kontokaks.rahavalja(1200)