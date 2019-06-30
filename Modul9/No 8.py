class SimpulPohonBiner():
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None
        
def cetakDataDanLevel(akar, level=-1):
    level += 1
    if akar is not None:
        print akar.data, "Level", level
        cetakDataDanLevel(akar.kiri,level)
        
cetakDataDanLevel(akar.kanan,level)

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

A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I
