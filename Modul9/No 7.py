class SimpulPohonBiner():
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def tinggiPohon(akar):
    if akar is None:
        return 0
    else:
        kiri = tinggiPohon(akar.kiri)
        kanan = tinggiPohon(akar.kanan)
        if kiri > kanan:
            return kiri+1
        else:
            return kanan+1

A = SimpulPohonBiner("Surakarta")
B = SimpulPohonBiner("Cimahi")
C = SimpulPohonBiner("Merauke")
D = SimpulPohonBiner("Salatiga")
E = SimpulPohonBiner("Magelang")
F = SimpulPohonBiner("Purworejo")
G = SimpulPohonBiner("Bogor")
H = SimpulPohonBiner("Klaten")
I = SimpulPohonBiner("Wonogiri")
J = SimpulPohonBiner("Halmahera")
