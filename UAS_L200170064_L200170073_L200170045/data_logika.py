from data_film import *

##Pengurutan data di Array dari A - Z Algoritma Mark Sort
##Pencarian Data Di Array Algoritma Linier Search

def pengurut_judul(A):
        
    if len(A) > 1:
        mid = len(A) // 2
        mid_Kiri = A[:mid]
        mid_Kanan = A[mid:]

        pengurut_judul(mid_Kiri)
        pengurut_judul(mid_Kanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(mid_Kiri) and j < len(mid_Kanan):
            if mid_Kiri[i][0] < mid_Kanan[j][0]:
                A[k] = mid_Kiri[i]
                i += 1
            else:
                A[k] = mid_Kanan[j]
                j += 1
            k += 1

        while i < len(mid_Kiri):
            A[k] = mid_Kiri[i]
            i += 1
            k += 1

        while j < len(mid_Kanan):
            A[k] = mid_Kanan[j]
            j += 1
            k += 1
            
        return A


def pengurut_sutradara(A):
        
    if len(A) > 1:
        mid = len(A) // 2
        mid_Kiri = A[:mid]
        mid_Kanan = A[mid:]

        pengurut_sutradara(mid_Kiri)
        pengurut_sutradara(mid_Kanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(mid_Kiri) and j < len(mid_Kanan):
            if mid_Kiri[i][1] < mid_Kanan[j][1]:
                A[k] = mid_Kiri[i]
                i += 1
            else:
                A[k] = mid_Kanan[j]
                j += 1
            k += 1

        while i < len(mid_Kiri):
            A[k] = mid_Kiri[i]
            i += 1
            k += 1

        while j < len(mid_Kanan):
            A[k] = mid_Kanan[j]
            j += 1
            k += 1
            
        return A


def linear_search_judul(myList,item):
    for i in range(len(myList)):
        if myList[i][0] == item:
            return i
    return -1


def pengurut_tanggal(A):
        
    if len(A) > 1:
        mid = len(A) // 2
        mid_Kiri = A[:mid]
        mid_Kanan = A[mid:]

        pengurut_tanggal(mid_Kiri)
        pengurut_tanggal(mid_Kanan)

        i = 0 ; j = 0 ; k = 0
        while i < len(mid_Kiri) and j < len(mid_Kanan):
            if mid_Kiri[i][2] < mid_Kanan[j][2]:
                A[k] = mid_Kiri[i]
                i += 1
            else:
                A[k] = mid_Kanan[j]
                j += 1
            k += 1

        while i < len(mid_Kiri):
            A[k] = mid_Kiri[i]
            i += 1
            k += 1

        while j < len(mid_Kanan):
            A[k] = mid_Kanan[j]
            j += 1
            k += 1
            
        return A

def precompute_max_prefix_suffix(A):
  result = [0] * (len(A) + 1)
  for k in range(2, len(A) + 1):
    l_minus_one = result[k-1]
    while l_minus_one > 0 and A[l_minus_one] != A[k-1]:
      l_minus_one = result[l_minus_one]
    if A[l_minus_one] == A[k-1]:
      result[k] = l_minus_one + 1
  return result


##def cari_judul(A):
##
##    for i < 0 ; n - m
    
