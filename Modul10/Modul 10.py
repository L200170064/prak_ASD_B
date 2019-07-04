#Nomer1 membuat fingsi ukuranPohon(akar) yang akan mendapat ukuran pohon biner
class simpulPohonBiner():
    def __init__(self,data):
        self.data = data
        self.kiri = None
        self.kanan = None

def ukuranPohon (akar):
    ukuran = 0
    if akar is not None :
        if akar.kiri is None and akar.kanan is None :
            ukuran += 1
        else :
            hasil =  ukuranPohon (akar.kiri)
            ukuran += hasil
            hasil = ukuranPohon(akar.kanan)
            ukuran += hasil
    return ukuran

A = simpulPohonBiner ("Ambarawa")
B = simpulPohonBiner ("Bantul")
C = simpulPohonBiner ("Denpasar")
D = simpulPohonBiner ("Palembang")
E = simpulPohonBiner ("Banten")
F = simpulPohonBiner ("Garut")
G = simpulPohonBiner ("Jakarta")
H = simpulPohonBiner ("Flores")
I = simpulPohonBiner ("Indramayu")
J = simpulPohonBiner ("Halmahera Timur")


A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I

#Nomer 2 membuat fungsi tinggi pohon(akar) yg akan mendapat ketinggian sebuah pohon biner
class simpulPohonBiner():
    def __init__(self,data):
        self.data = data
        self.kiri = None
        self.kanan = None

def tinggiPohon(akar):
    if akar is None :
        return 0
    else:
        kiri = tinggiPohon(akar.kiri)
        kanan = tinggiPohon(akar.kanan)
        if kiri > kanan:
            return kiri+1
        else:
            return kanan+1

A = simpulPohonBiner ("Ambarawa")
B = simpulPohonBiner ("Bantul")
C = simpulPohonBiner ("Denpasar")
D = simpulPohonBiner ("Palembang")
E = simpulPohonBiner ("Banten")
F = simpulPohonBiner ("Garut")
G = simpulPohonBiner ("Jakarta")
H = simpulPohonBiner ("Flores")
I = simpulPohonBiner ("Indramayu")
J = simpulPohonBiner ("Halmahera Timur")

#3 membuat fungsi cetakDataDanLevel()

class simpulPohonBiner():
    def __init__(self,data):
        self.data = data
        self.kiri = None
        self.kanan = None

def cetakDataDanLevel (akar, level=-1):
    level += 1
    if akar is not None:
        print akar.data, "Level", level
        cetakDataDanLevel (akar.kiri, level)
        cetakDataDanLevel (akar.kanan,level)

A = simpulPohonBiner ("Ambarawa")
B = simpulPohonBiner ("Bantul")
C = simpulPohonBiner ("Denpasar")
D = simpulPohonBiner ("Palembang")
E = simpulPohonBiner ("Banten")
F = simpulPohonBiner ("Garut")
G = simpulPohonBiner ("Jakarta")
H = simpulPohonBiner ("Flores")
I = simpulPohonBiner ("Indramayu")
J = simpulPohonBiner ("Halmahera Timur")

A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I
