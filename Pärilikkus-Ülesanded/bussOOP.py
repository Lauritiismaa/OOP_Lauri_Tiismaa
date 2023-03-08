#Lauri Tiismaa IT-21 28.02.2023


class soiduk:
    
    
    def __init__(self, maxkiirus, nimi, istekohtadearv):
        self.maxkiirus = maxkiirus
        self.nimi = nimi
        self.istekohtadearv = istekohtadearv


class buss(soiduk):
    
    
    def __init__(self, maxkiirus, nimi, istekohtadearv, piletihind, soitjatearv):
        super().__init__(maxkiirus, nimi, istekohtadearv)
        self.piletihind = piletihind
        self.soitjatearv = soitjatearv
        
        
    def andmed(self):
        print("Bussi maxkiirus on:", self.maxkiirus,", Bussiliini nimeks on:", self.nimi,", Bussis on istekohti:", self.istekohtadearv,
              ", piletihind on:", self.piletihind,", sõitjate arv on:", self.soitjatearv)
        
        
    def ostapilet(self, piletid):
        if (self.istekohtadearv) - (self.soitjatearv) >= piletid:
            self.soitjatearv += (piletid)
            print("Ostsite " + str(piletid) + " Piletit")
        else:
            print("bussis pole piisavalt kohti et niipalju pileteid osta")
        
        
buss1 = buss(120, "Tallinn - Pärnu", 100, 10, 70)
buss1.ostapilet(20)
buss1.andmed()
    
    