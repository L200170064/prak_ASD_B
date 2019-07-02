class data_film(object):
    
    """class data untuk film"""
    
    def __init__(self, judul_film, nama_sutradara, tanggal_rillis):
        self.judul = judul_film
        self.sutradara = nama_sutradara
        self.tanggal = tanggal_rillis

    def __repr__(self):
        info = self.judul + ', ' + self.sutradara + ', ' + self.tanggal
        return info

    def __str__(self):
        info = self.judul + ', ' + self.sutradara + ', ' + self.tanggal
        return info

class my_Array(object):
    
    """class untuk Array pada film"""

    def __init__(self):
        self.index = 10 * [None]
        
    def __getitem__(self, item):
        getData = self.index[item]
        return getData
    
    def __setitem__(self, key, value):
        self.index[key] = value

#-------------------------------------------------------------------------------#

film_1 = data_film('THE FATE OF THE FURIOUS',
                   'GARY GRAY',
                   '14 APRIL 2017')
film_2 = data_film('STAND BY ME DORAEMON',
                   'RUCHI YAGI',
                   '8 AAGUSTUS 2014')
film_3 = data_film('BLACK PANTHER',
                   'RYAN COGLER',
                   '16 FEBRUARI 2018')
film_4 = data_film('TITANIC',
                   'JAMES CAMERON',
                   '19 DESEMBER 1997')
film_5 = data_film('AVENGER END GAME',
                   'ANTHONY RUSSO',
                   '22 APRIL 2019')
film_6 = data_film('CAPTAIN MARVEL',
                   'ANNA BODEN',
                   '28 MARET 2019')
film_7 = data_film('TRAIN TO BUSAN',
                   'YEON SANG HO',
                   '20 JULI 2016')
film_8 = data_film('T A G',
                   'SION SONO',
                   '11 Juli 2015')
film_9 = data_film('SADAKO 3D',
                   'TSUTOMO TAKAHASI',
                   '12 MEI 2012')
film_10 = data_film('SCHOOL GIRL COMPLEX',
                   'YUICHI ONUMA',
                   '17 AGUSTUS 2013')

#-------------------------------------------------------------------------------#

akumulasi_data = my_Array()

akumulasi_data[0] = film_1
akumulasi_data[1] = film_2
akumulasi_data[2] = film_3
akumulasi_data[3] = film_4
akumulasi_data[4] = film_5
akumulasi_data[5] = film_6
akumulasi_data[6] = film_7
akumulasi_data[7] = film_8
akumulasi_data[8] = film_9
akumulasi_data[9] = film_10

akumulasi_data_judul = my_Array()

akumulasi_data_judul[0] = film_1.judul
akumulasi_data_judul[1] = film_2.judul
akumulasi_data_judul[2] = film_3.judul
akumulasi_data_judul[3] = film_4.judul
akumulasi_data_judul[4] = film_5.judul
akumulasi_data_judul[5] = film_6.judul
akumulasi_data_judul[6] = film_7.judul
akumulasi_data_judul[7] = film_8.judul
akumulasi_data_judul[8] = film_9.judul
akumulasi_data_judul[9] = film_10.judul

akumulasi_data_sutradara = my_Array()

akumulasi_data_sutradara[0] = film_1.sutradara
akumulasi_data_sutradara[1] = film_2.sutradara
akumulasi_data_sutradara[2] = film_3.sutradara
akumulasi_data_sutradara[3] = film_4.sutradara
akumulasi_data_sutradara[4] = film_5.sutradara
akumulasi_data_sutradara[5] = film_6.sutradara
akumulasi_data_sutradara[6] = film_7.sutradara
akumulasi_data_sutradara[7] = film_8.sutradara
akumulasi_data_sutradara[8] = film_9.sutradara
akumulasi_data_sutradara[9] = film_10.sutradara

akumulasi_data_tanggal = my_Array()

akumulasi_data_tanggal[0] = film_1.tanggal
akumulasi_data_tanggal[1] = film_2.tanggal
akumulasi_data_tanggal[2] = film_3.tanggal
akumulasi_data_tanggal[3] = film_4.tanggal
akumulasi_data_tanggal[4] = film_5.tanggal
akumulasi_data_tanggal[5] = film_6.tanggal
akumulasi_data_tanggal[6] = film_7.tanggal
akumulasi_data_tanggal[7] = film_8.tanggal
akumulasi_data_tanggal[8] = film_9.tanggal
akumulasi_data_tanggal[9] = film_10.tanggal

akumulasi_data_final = my_Array()

akumulasi_data_final[0] = [film_1.judul, film_1.sutradara, film_1.tanggal]
akumulasi_data_final[1] = [film_2.judul, film_2.sutradara, film_2.tanggal]
akumulasi_data_final[2] = [film_3.judul, film_3.sutradara, film_3.tanggal]
akumulasi_data_final[3] = [film_4.judul, film_4.sutradara, film_4.tanggal]
akumulasi_data_final[4] = [film_5.judul, film_5.sutradara, film_5.tanggal]
akumulasi_data_final[5] = [film_6.judul, film_6.sutradara, film_6.tanggal]
akumulasi_data_final[6] = [film_7.judul, film_7.sutradara, film_7.tanggal]
akumulasi_data_final[7] = [film_8.judul, film_8.sutradara, film_8.tanggal]
akumulasi_data_final[8] = [film_9.judul, film_9.sutradara, film_9.tanggal]
akumulasi_data_final[9] = [film_10.judul, film_10.sutradara, film_10.tanggal]

#-------------------------------------------------------------------------------#

data_semua = [akumulasi_data[0], akumulasi_data[1],
              akumulasi_data[2], akumulasi_data[3],
              akumulasi_data[4], akumulasi_data[5],
              akumulasi_data[6], akumulasi_data[7],
              akumulasi_data[8], akumulasi_data[9]]

data_final = [akumulasi_data_final[0], akumulasi_data_final[1],
              akumulasi_data_final[2], akumulasi_data_final[3],
              akumulasi_data_final[4], akumulasi_data_final[5],
              akumulasi_data_final[6], akumulasi_data_final[7],
              akumulasi_data_final[8], akumulasi_data_final[9]]

data_ulti = [akumulasi_data_judul[0], akumulasi_data_sutradara[0],
             akumulasi_data_tanggal[0], akumulasi_data_judul[1],
             akumulasi_data_sutradara[1], akumulasi_data_tanggal[1],
             akumulasi_data_judul[2], akumulasi_data_sutradara[2],
             akumulasi_data_tanggal[2], akumulasi_data_judul[3],
             akumulasi_data_sutradara[3], akumulasi_data_tanggal[3],
             akumulasi_data_judul[4], akumulasi_data_sutradara[4],
             akumulasi_data_tanggal[4], akumulasi_data_judul[5],
             akumulasi_data_sutradara[5], akumulasi_data_tanggal[5],
             akumulasi_data_judul[6], akumulasi_data_sutradara[6],
             akumulasi_data_tanggal[6], akumulasi_data_judul[7],
             akumulasi_data_sutradara[7], akumulasi_data_tanggal[7],
             akumulasi_data_judul[8], akumulasi_data_sutradara[8],
             akumulasi_data_tanggal[8], akumulasi_data_judul[9],
             akumulasi_data_sutradara[9], akumulasi_data_tanggal[9]]

data_judul = [akumulasi_data_judul[0], akumulasi_data_judul[1],
              akumulasi_data_judul[2], akumulasi_data_judul[3],
              akumulasi_data_judul[4], akumulasi_data_judul[5],
              akumulasi_data_judul[6], akumulasi_data_judul[7],
              akumulasi_data_judul[8], akumulasi_data_judul[9]]

data_sutradara = [akumulasi_data_sutradara[0], akumulasi_data_sutradara[1],
                akumulasi_data_sutradara[2], akumulasi_data_sutradara[3],
                akumulasi_data_sutradara[4], akumulasi_data_sutradara[5],
                akumulasi_data_sutradara[6], akumulasi_data_sutradara[7],
                akumulasi_data_sutradara[8], akumulasi_data_sutradara[9]]

data_tanggal = [akumulasi_data_tanggal[0], akumulasi_data_tanggal[1],
                akumulasi_data_tanggal[2], akumulasi_data_tanggal[3],
                akumulasi_data_tanggal[4], akumulasi_data_tanggal[5],
                akumulasi_data_tanggal[6], akumulasi_data_tanggal[7],
                akumulasi_data_tanggal[8], akumulasi_data_tanggal[9]]
