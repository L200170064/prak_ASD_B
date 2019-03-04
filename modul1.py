""" Nama : OKI KUS MAHESA
    NIM  : L200170064
    Kelas: B """

#nomor1
def cetakSiku(x) :
    for i in range(x+1) :
        print(("x")*i)

#nomor2
def gambarlahPersegiEmpat(x, y) :
    for i in range(x) :
        if i == 0 or i == x-1 :
            print(("@")*y)
        else:
            print(("@")+(" ")*(y-2)+("@"))

#nomor3.a
def jumlahHurufVokal (a):
    vok = "aiueo"
    jumlah = 0
    for x in a :
        if x.lower() in vok:
            jumlah +=1
    return (len(a),jumlah)

#nomor3.b
def jumlahHurufKonsonan (a):
    vok = "aiueo"
    jumlah = 0
    for x in a :
        if x.lower() not in vok:
            jumlah +=1
    return (len(a),jumlah)

#nomor4
def rerata(b):
    hasil = float(sum(b))/float(len(b))
    return hasil

#nomor5
from math import sqrt as sq
def apakahPrima(n):

        n = int(n)
        assert n >= 0
        primaKecil = [2, 3, 5 ,7, 11]
        bknPrimaKecil = [0, 1, 4, 6, 8, 9, 10]
        # mengecek bilangan prima selalu lebih besar dari 1
        if n in primaKecil:
                return True
        elif n in bknPrimaKecil:
                return False
        else:
                # mengecek faktor pembagi dengan operasi modulus
                for i in range(2,int(sq(n))+1):
                        if (n % i) == 0:
                                print (n,"bukan bilangan prima")
                                print ("karena", n,"dikalikan",n//n,"hasilnya adalah",n)
                                break
                else:
                        print (n,"adalah bilangan prima")

#nomor6
low = 2
up = 1000
for num in range(low,up+1):
    if num>1:
        for i in range(2,num):
            if(num%i == 0):
                break
        else:
            print(num)
            
#nomor7
def faktorPrima(x) : # x adalah bilangan yang diinputkan untuk di dicari faktor prima nya
    a = []  #untuk menyimpan bilangan prima
    b = []  #untuk menyimpan faktor prima dari bilangan yg diinputkan
    hasil = 0
    bil = x
    prima =True
    for i in range(2,x):
        prima = True
        for u in range(2, i) :
            if i % u == 0 :
               prima = False
        if prima :
            a.append(i)     #menambahkan bilangan prima ke variabel a
    idx = 0
    while bil > 1 :      
        try:    #try untuk mengatasi error ketika index out of range,msal list pnya 5 data maka ketika mengindex data ke6 akan error.
            if (bil%a[idx]) == 0 : # a[idx] untuk mengambil bilangan prima dari list a berdasarkan indexing nya
                hasil = bil/a[idx]
                bil = hasil
                b.append(a[idx])#memasukkan faktor primanya ke 'b'
            else :
                idx = idx + 1
        except IndexError :
            break
    print (b)

#nomor8
def apakahTerkandung(h,k):
    return h.lower() in k.lower()

#nomor9
def ProgCetakAngka(n):
    i = 0
    for i in range (n):
        if i % 3 == 2 and i % 5 == 4:
            print("Python UMS")
        elif i % 3 == 2:
            print("Python")
        elif i % 5 == 4:
            print("UMS")
        else:
            print(i + 1)

#nomor10
def selesaikanABC(a,b,c):
    if a <= 0 and b <= 0 and c <= 0:
        print("Determinannya Positif. Persamaan mempunyai akar Real")
    else:
        print("Determinannya Negatif. Persamaan tidak mempunyai akar Real")
        
#nomor11
import datetime;
def apakahKabisat(n):
    if (n % 4) == 0:
        if (n % 100) == 0:
            if (n % 400) == 0:
                print ("Tahun Kabisat")
            else:
                print("Bukan Tahun Kabisat")
        else:
            print("Tahun Kabisat")
    else:
        print("Bukan Tahun Kabisat")

#nomor12
angka = 25
    
print("Permainan Tebak Angka")
print("Ssya  Menyimpan Sebuah Angka bulat Antara 1 sampai 100. Coba tebak")

while angka != -1:
    
    masukkan =  int(input("Masukan Tebakan :>"))

    if masukkan == angka:
        print("Ya. Anda Benar", angka)
        break
    elif masukkan > angka:
        print("Itu Terlalu Besar. Coba Lagi")
    elif masukkan < angka:
        print("Itu Terlalu Kecil. Coba Lagi")

#nomor13
def katakan(bil):
    angka = ["","Satu ","Dua ","Tiga ","Empat ","Lima ","Enam ",
             "Tujuh ","Delapan ","Sembilan ","Sepuluh ","Sebelas "]
    hasil = ""
    n = int(bil)
    if n >= 0 and n <= 11:

 
        hasil = angka[n]
    elif n < 20:
        hasil = katakan(n-10) + "Belas "
    elif n < 100:
        hasil = katakan(n/10) + "Puluh " + katakan(n%10)
    elif n < 200:
        hasil = "Seratus " + katakan(n-100)
    elif n < 1000:
        hasil = katakan(n/100) + "Ratus " + katakan(n%100)
    elif n < 2000:
        hasil = "Seribu " + katakan(n-1000)
    elif n < 1000000:
        hasil = katakan(n/1000) + "Ribu " + katakan(n%1000) 
    elif n < 1000000000:
        hasil = katakan(n/1000000) + "Juta " + katakan(n%1000000)
    elif n > 1000000000:
        hasil = 'Maaf, program tidak membaca angka lebih dari Satu Milyar'
    return hasil


a = 1
while a != 0:
    a = input(' Masukkan angka dari 1 sd 1.000.000.000: ')
    huruf = katakan(a)
    print(huruf +'Rupiah')
    break

#nomor14
def formatRupiah(n):
    y = str(n)
    if len(y) <= 3 :
        return 'Rp ' + y     
    else :
        p = y[-3:]
        q = y[:-3]
        return   (formatRupiah(q) + '.' + p)
        print ('Rp' +  (formatRupiah(q)) + '.' + p) 
