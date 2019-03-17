""" Nama  : OKI KUS MAHESA
    Nim   : L200170064
    Kelas : B """
    

# No1 a
matrix = [[1,5,6],[2,5,9],[5,6,2]]
a = len(matrix)
b = len(matrix[0])
"""Fungsi isi dan ukuran Matriks tetap Konsisten"""
def Konsisten():
    if a == b:
        print("Matrix Konsisten")
    else:
        print("Matrix tidak Konsisten")

# b
matrix = [[1,5,6,8],[1,2,5,9],[7,5,6,2]]
a = len(matrix)
b = len(matrix[0])
"""Fungsi untuk Mengambil Ukuran Matrixnya"""
def MUM():
    print('Ukuran Matrix adalah ' , a , ' x ' , b)
        
# c
matrix = [[1,5,6],[2,5,9],[5,6,2]]
matrix2 = [[1,5,6],[2,5,9],[5,6,2]]
a = len(matrix)
aa = len(matrix[0])
b = len(matrix2)
bb = len(matrix2[0])
perkalian = ((a*aa)+(b*bb))
def MJ2M():
    print(perkalian)

# d
matrix = [[1,5,6],[2,5,9],[5,6,2]]
matrix2 = [[1,5,6],[2,5,9],[5,6,2]]
a = len(matrix)
aa = len(matrix[0])
b = len(matrix2)
bb = len(matrix2[0])
perkalian = ((a+aa)*(b+bb))
def M2M():
    print(perkalian)

# e
matrixA = ([3, 5],[4, 8])
det_A_axd = matrixA[0][0] * matrixA[1][1]
det_A_bxc = matrixA[0][1] * matrixA[1][0]
def M_A():
    "Fungsi Menghitung Determinan Matrix A"
    print("Determinan Matrix A =", det_A_axd - det_A_bxc)
    





# No2
# a
def buatNo1(m): 
    for row in range(0, m): 
        for col in range(0, m): 
            if (row == col): 
                print("0 ", end=" ") 
            else: 
                print("0 ", end=" ") 
        print() 

# b
def buatIdentitas(m): 
    for row in range(0, m): 
        for col in range(0, m): 
            if (row == col): 
                print("1 ", end=" ") 
            else: 
                print("0 ", end=" ") 
        print() 






# No3
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # a
    def cari(head, yang_dicari):
        temp = head
        while temp != None:
            if temp.data == yang_dicari:
                return temp
            temp = temp.next
        return Node(None)
        
    # b
    def tambahDepan(head):
        temp = Node("tambah depan ", head)
        return temp

    # c
    def tambahakhir(head):
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = Node("tambah akhir")
        return head

    # d
    def tambah(head, posisi):
        "Menambahkan simpul terserah posisi"
        temp = head
        while temp != None:
            if temp.next.data == posisi:
                temp_belakang = temp.next
                temp.next = Node("tambah tersrah ", temp_belakang)
                return head
            temp = temp.next

    # e
    def hapus(head, posisi):
        while temp != None:
            if temp.next.data == posisi:
                temp.belakang = temp.next.next
                temp.next = temp_belakang
                return head
            temp = temp.next
        return None






# No4
class DNode(object):
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    # a
    def cetakSimpul(self, temp):
        while temp is not None:
            print(temp.data)
            temp = temp.next
        while temp is not None:
            print(temp.data)
            temp = temp.prev
    
    # b
    def tambahAwal(self, temp):
        node = Node(temp, self)
        node.next = self.next
        self.next = node
        if self.prev == None:
            self.prev = node
        self.len += 1

    # c
    def tambahAkhir(self, temp):
        node = Node(temp, self)
        node.prev = self.prev
        self.prev = node
        if self.next == None:
            self.next = node
        self.len += 1

    
