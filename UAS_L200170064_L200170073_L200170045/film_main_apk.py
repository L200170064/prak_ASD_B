from PyQt5 import QtCore, QtGui, QtWidgets
import re
from data_film import *
from data_logika import *

class Ui_halaman_utama(object):

##___________________________________________________________________________________________

    def setupUi(self, halaman_utama):

        halaman_utama.setObjectName("halaman_utama")
        halaman_utama.resize(795, 370)
        halaman_utama.setStyleSheet("QWidget { background-color : red}")

        self.centralwidget = QtWidgets.QWidget(halaman_utama)
        self.centralwidget.setObjectName("centralwidget")

##___________________________________________________________________________________________

        self.frame_table = QtWidgets.QFrame(self.centralwidget)
        self.frame_table.setGeometry(QtCore.QRect(260, 15, 500, 260))
        self.frame_table.setStyleSheet("QWidget { background-color : blue; color : white; }")
        self.frame_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_table.setObjectName("frame_table")

        # Table Content
        self.table_data = QtWidgets.QTableWidget(self.frame_table)
        self.table_data.setGeometry(QtCore.QRect(0, 0, 500, 260))
        self.table_data.setStyleSheet("QWidget { background-color : white; color : blue; }")
        self.table_data.setRowCount(0)
        self.table_data.setColumnCount(3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setPointSize(11)
        self.table_data.setFont(font)
        self.table_data.setObjectName("table_data")
        self.table_data.setColumnCount(3)
        self.table_data.setRowCount(0)
##___________________________________________________________________________________________

        # Data Film Pada Table :

        # Header
        
        header = ['Judul Film', 'Sutradara', 'Tanggal Rillis']
        self.table_data.setHorizontalHeaderLabels(header)
        self.table_data.horizontalHeader().setStyleSheet("QWidget { background-color : white; color : blue; }")
        font = QtGui.QFont()
        font.setFamily("Courir New")
        font.setPointSize(9)
        font.setBold(True)
        self.table_data.horizontalHeader().setFont(font)
        self.table_data.setColumnWidth(0,200)
        self.table_data.setColumnWidth(1,200)
        self.table_data.setColumnWidth(2,200)
        self.table_data.verticalHeader().setStyleSheet("QWidget { background-color : white; color : blue; }")
        font = QtGui.QFont()
        font.setFamily("Courir New")
        font.setPointSize(9)
        font.setBold(True)
        self.table_data.verticalHeader().setFont(font)
        self.table_data.setStyleSheet("QWidget { background-color : yellow; color : green; }")
        font = QtGui.QFont()
        font.setFamily("Courir New")
        font.setBold(True)
        font.setPointSize(8)
        self.table_data.setFont(font)

        for i in range(len(data_final)):
            row_kosong = self.table_data.rowCount()

            self.table_data.insertRow(row_kosong)
            self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
            self.table_data.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
            self.table_data.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))

##___________________________________________________________________________________________

        # Frame Urut
        self.frame_urut = QtWidgets.QFrame(self.centralwidget)
        self.frame_urut.setGeometry(QtCore.QRect(140, 278, 600, 71))
        self.frame_urut.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_urut.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_urut.setObjectName("frame_urut")

##___________________________________________________________________________________________

        # Tombol pengurutan judul
        self.tombol_urut_judul = QtWidgets.QPushButton(self.frame_urut)
        self.tombol_urut_judul.setGeometry(QtCore.QRect(230, 20, 101, 31))
        self.tombol_urut_judul.setStyleSheet("QWidget { background-color : white; color : #4d004d; }")
        self.tombol_urut_judul.setObjectName("tombol_urut_judul")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.tombol_urut_judul.setFont(font)

##___________________________________________________________________________________________
        
        #Label Urut Berdasarkan
        self.label_urut = QtWidgets.QLabel(self.frame_urut)
        self.label_urut.setGeometry(QtCore.QRect(80, 19, 120, 31))
        self.label_urut.setStyleSheet("QWidget { background-color : red; color : white; }")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_urut.setFont(font)
        self.label_urut.setObjectName("label_urut")

##___________________________________________________________________________________________

        # Tombol pengurutan sutradara
        self.tombol_urut_sutradara = QtWidgets.QPushButton(self.frame_urut)
        self.tombol_urut_sutradara.setGeometry(QtCore.QRect(350, 20, 106, 31))
        self.tombol_urut_sutradara.setStyleSheet("QWidget { background-color : white; color : #4d004d; }")
        self.tombol_urut_sutradara.setObjectName("tombol_urut_sutradara")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12 )
        font.setBold(True)
        self.tombol_urut_sutradara.setFont(font)

##___________________________________________________________________________________________

        # Tombol Pengurutan tanggal
        self.tombol_urut_tanggal = QtWidgets.QPushButton(self.frame_urut)
        self.tombol_urut_tanggal.setGeometry(QtCore.QRect(475, 20, 101, 31))
        self.tombol_urut_tanggal.setStyleSheet("QWidget { background-color : white; color : #4d004d; }")
        self.tombol_urut_tanggal.setObjectName("tombol_urut_tanggal")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.tombol_urut_tanggal.setFont(font)

##___________________________________________________________________________________________
        
        # Frame Cari
        self.frame_cari = QtWidgets.QFrame(self.centralwidget)
        self.frame_cari.setGeometry(QtCore.QRect(25, 20 , 231, 260))
        self.frame_cari.setStyleSheet("QWidget { background-color : red}")
        self.frame_cari.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cari.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cari.setObjectName("frame_cari")

        self.label_cari = QtWidgets.QLabel(self.frame_cari)
        self.label_cari.setGeometry(QtCore.QRect(20, 10, 190, 30))
        self.label_cari.setStyleSheet("QWidget { color : white }")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        self.label_cari.setFont(font)
        self.label_cari.setObjectName("label_cari")

##___________________________________________________________________________________________

        # Text Box Pencarian
        self.textBox_cari = QtWidgets.QLineEdit(self.frame_cari)
        self.textBox_cari.setGeometry(QtCore.QRect(20, 50, 181, 27))
        self.textBox_cari.setStyleSheet("QWidget { background-color : white}")
        self.textBox_cari.setObjectName("textBox_cari")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        self.textBox_cari.setFont(font)

##___________________________________________________________________________________________

        # Tombol Pencarian
        self.tombol_cari_judul = QtWidgets.QPushButton(self.frame_cari)
        self.tombol_cari_judul.setGeometry(QtCore.QRect(20, 100, 120, 35))
        self.tombol_cari_judul.setStyleSheet("QWidget { background-color : white; color : #4d004d; }")
        self.tombol_cari_judul.setObjectName("tombol_cari_judul")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.tombol_cari_judul.setFont(font)

        # Tombol Pencarian 2
        self.tombol_cari_sutradara = QtWidgets.QPushButton(self.frame_cari)
        self.tombol_cari_sutradara.setGeometry(QtCore.QRect(20, 155, 120, 35))
        self.tombol_cari_sutradara.setStyleSheet("QWidget { background-color : white; color : #4d004d; }")
        self.tombol_cari_sutradara.setObjectName("tombol_cari_sutdradara")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.tombol_cari_sutradara.setFont(font)

        # Tombol Pencarian 3
        self.tombol_cari_tanggal = QtWidgets.QPushButton(self.frame_cari)
        self.tombol_cari_tanggal.setGeometry(QtCore.QRect(20, 205, 120, 35))
        self.tombol_cari_tanggal.setStyleSheet("QWidget { background-color : white; color : #4d004d; }")
        self.tombol_cari_tanggal.setObjectName("tombol_cari_tanggal")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        self.tombol_cari_tanggal.setFont(font)

        halaman_utama.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(halaman_utama)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 795, 21))
        self.menubar.setObjectName("menubar")

        halaman_utama.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(halaman_utama)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet("QWidget { background-color : white}")

        halaman_utama.setStatusBar(self.statusbar)

        self.retranslateUi(halaman_utama)
        QtCore.QMetaObject.connectSlotsByName(halaman_utama)
##___________________________________________________________________________________________

        # Function Connect
        
        self.tombol_urut_judul.clicked.connect(self.action_pengurutan_judul)
        self.tombol_urut_sutradara.clicked.connect(self.action_pengurutan_sutradara)
        self.tombol_urut_tanggal.clicked.connect(self.action_pengurutan_tanggal)
        self.tombol_cari_judul.clicked.connect(self.action_cari_judul)
        self.tombol_cari_sutradara.clicked.connect(self.action_cari_sutradara)
        self.tombol_cari_tanggal.clicked.connect(self.action_cari_tanggal)
        

##___________________________________________________________________________________________

    # Function pencarian judul

    def action_cari_judul(self):
        self.table_data.setRowCount(0)
        for i in range(len(data_final)):
            if self.textBox_cari.text().upper() in data_final[i][0]:
                row_kosong = self.table_data.rowCount()
                self.table_data.insertRow(row_kosong)
                self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
                self.table_data.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
                self.table_data.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))
        return i

        def tambah(self):         
            row_kosong = self.table_data.rowCount()
            self.table_data.insertRow(row_kosong)
            self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(self.textBox_cari.text()))

##___________________________________________________________________________________________

    # Function pencarian sutradara

    def action_cari_sutradara(self):
        self.table_data.setRowCount(0)
        for i in range(len(data_final)):
            if self.textBox_cari.text().upper() in data_final[i][1]:
                row_kosong = self.table_data.rowCount()
                self.table_data.insertRow(row_kosong)
                self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
                self.table_data.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
                self.table_data.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))
        return i

        def tambah(self):         
            row_kosong = self.table_data.rowCount()
            self.table_data.insertRow(row_kosong)
            self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(self.textBox_cari.text()))

##___________________________________________________________________________________________

    # Function pencarian tanggal

    def action_cari_tanggal(self):
        target = self.textBox_cari.text()
        self.table_data.setRowCount(0)
        for i in range(len(data_final)):
            if self.textBox_cari.text().upper() in data_final[i][2]:
                row_kosong = self.table_data.rowCount()
                self.table_data.insertRow(row_kosong)
                self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
                self.table_data.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
                self.table_data.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))

        def tambah(self):         
            row_kosong = self.table_data.rowCount()
            self.table_data.insertRow(row_kosong)
            self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(self.textBox_cari.text()))
            
##___________________________________________________________________________________________        

    # Function pengurut judul
    
    def action_pengurutan_judul(self):
        target = pengurut_judul(data_final)
        self.table_data.setRowCount(0)
        for i in range(len(data_final)):
            row_kosong = self.table_data.rowCount()
            self.table_data.insertRow(row_kosong) 
            self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
            self.table_data.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
            self.table_data.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))


    def tambah_cell(self):
        row_kosong = self.table_data.rowCount()
        self.table_data.insertRow(row_kosong)
        self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(''))

##___________________________________________________________________________________________  

    # Function pengurut sutradara

    def action_pengurutan_sutradara(self):
        target = pengurut_sutradara(data_final)
        self.table_data.setRowCount(0)
        for i in range(len(data_final)):
            row_kosong = self.table_data.rowCount()
            self.table_data.insertRow(row_kosong) 
            self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
            self.table_data.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
            self.table_data.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))

    def tambah_cell(self):
        row_kosong = self.table_data.rowCount()
        self.table_data.insertRow(row_kosong)
        self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(''))

##___________________________________________________________________________________________

    # Function pengurut tanggal

    def action_pengurutan_tanggal(self):
        target = pengurut_tanggal(data_final)
        self.table_data.setRowCount(0)
        for i in range(len(data_final)):
            row_kosong = self.table_data.rowCount()
            self.table_data.insertRow(row_kosong) 
            self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(data_final[i][0]))
            self.table_data.setItem(row_kosong, 1, QtWidgets.QTableWidgetItem(data_final[i][1]))
            self.table_data.setItem(row_kosong, 2, QtWidgets.QTableWidgetItem(data_final[i][2]))

    def tambah_cell(self):
        row_kosong = self.table_data.rowCount()
        self.table_data.insertRow(row_kosong)
        self.table_data.setItem(row_kosong, 0, QtWidgets.QTableWidgetItem(''))

##___________________________________________________________________________________________
    
    def retranslateUi(self, halaman_utama):

        _translate = QtCore.QCoreApplication.translate

        halaman_utama.setWindowTitle(_translate("halaman_utama", "F I L M"))

        self.tombol_urut_judul.setText(_translate("halaman_utama", "Judul"))

        self.label_urut.setText(_translate("halaman_utama", "S o r t  B y  : "))

        self.tombol_urut_sutradara.setText(_translate("halaman_utama", "Sutradara"))

        self.tombol_urut_tanggal.setText(_translate("halaman_utama", "Tanggal"))

        self.label_cari.setText(_translate("halaman_utama", "S e a r c h i n g"))

        self.tombol_cari_judul.setText(_translate("halaman_utama", "Judul"))

        self.tombol_cari_sutradara.setText(_translate("halaman_utama", "Sutradara"))

        self.tombol_cari_tanggal.setText(_translate("halaman_utaman", "Tanggal"))

##___________________________________________________________________________________________


if __name__ == "__main__":

    import sys

    app = QtWidgets.QApplication(sys.argv)

    halaman_utama = QtWidgets.QMainWindow()

    ui = Ui_halaman_utama()
    ui.setupUi(halaman_utama)

    halaman_utama.show()

    sys.exit(app.exec_())

