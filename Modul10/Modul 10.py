import timeit
import matplotlib.pyplot as plt

## Ini fungsi nested loop yang akan diuji:
def kalangBersusuh(n):
     for i in range(n):
         for j in range(n):
              i+j

## Ini fungsi pengujinya:
def ujiKalangBersusuh(n):
    ls=[]
    jangkauan = range(1,n+1)
    siap = "from __main__ import kalangBersusuh"
    for i in jangkauan:
        #print(’i =’,i) # baris ini bisa dihidupkan atau dimatikan
        t=timeit.timeit("kalangBersusuh(" + str(i) +")", setup=siap, number=1)
        ls.append(t)
    return ls

## Pemanggilan pengujian
n = 1000
LS = ujiKalangBersusuh(n) # dari 1 sampai 1000.
## LS adalah list hasil uji kecepatan, dari n sedikit ke banyak

## Menggambar grafik. Di bawah ini saja yang diulang saat me-nyetel skala
plt.plot(LS) # Mem-plot hasil uji
skala = 7700000 # <------ Setel skala ini sesuai hasilmu
plt.plot([x*x/skala for x in range(1,n+1)]) # Grafik x^2 untuk pembanding.
plt.show() # Tunjukkan plotnya
