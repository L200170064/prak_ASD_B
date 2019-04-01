""" NAMA  : OKI KUS MAHESA
    NIM   : L200170064
    KELAS : B """
    
# ______________________________________________________________________________________________________________________________________
# No1
class MhsTif(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku
        
c0 = MhsTif("Ika",10,"Sukoharjo", 240000)
c1 = MhsTif("Budi",51,"Sragen", 230000)
c2 = MhsTif("Ahmad",2,"Surakarta", 250000)
c3 = MhsTif("Chandra",18,"Surakarta", 235000)
c4 = MhsTif("Eka",4,"Boyolali", 240000)
c5 = MhsTif("Fandi",31,"Salatiga", 250000)
c6 = MhsTif("Deni",13,"Klaten", 245000)
c7 = MhsTif("Galuh",5,"Wonogiri", 245000)
c8 = MhsTif("Janto",23,"Klaten", 245000)
c9 = MhsTif("Hasan",64,"Karanganyar", 270000)
c10 = MhsTif("Khalid",29,"Purwodadi", 265000)

Daftar =[c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def ambilNim():
    a = []
    for i in Daftar:
        a.append(i.nim)
    return a

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil
    
def urutkanNim(n):
    a = len(n)
    for i in range(a - 1):
        indexKecil = cariPosisiYangTerkecil(n, i, a)
        if indexKecil != i:
            swap(n, i, indexKecil)

o = ambilNim()
k = urutkanNim(o)
i = o
print(o)

# ______________________________________________________________________________________________________________________________________
# No2
a = [2, 4, 5, 10, 13, 18, 23, 29, 31, 51, 64]
b = [3, 7, 6, 11, 14, 19, 24, 30, 32, 52, 65]
m = a
n = b

def gabungAray():
    c = []
    for i in m:
        c.append(i)
    for j in n:
        c.append(j)
    return c

def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil
    
# No2
def arrayC(n):
    a = len(n)
    for i in range(a - 1):
        indexKecil = cariPosisiYangTerkecil(n, i, a)
        if indexKecil != i:
            swap(n, i, indexKecil)


o = gabungAray()
k = arrayC(o)
i = o
print(i)

# ______________________________________________________________________________________________________________________________________
# No3
def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def cariPosisiYangTerkecil(A, dariSini, sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

def bubleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiYangTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
            A[pos] = nilai

# No3
from time import time as detak
##from random import shuffle as kocok
k = range(1, 6001)
##kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw=detak();bubleSort(u_bub);ak=detak();print('bubble: %g detik' %(ak-aw));
aw=detak();selectionSort(u_sel);ak=detak();print('selection: %g detik' %(ak-aw));
aw=detak();insertionSort(u_ins);ak=detak();print('insertion: %g detik' %(ak-aw));
