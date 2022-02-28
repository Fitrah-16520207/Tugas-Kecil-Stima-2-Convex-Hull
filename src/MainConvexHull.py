import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from MathConvexHull import *
from UtilConvexHull import *


class ConvexHull:                                       # Objek convex hull
    def __init__(convex,listTitik):                     #Inisialisasi objek convex hull 
        convex.list = listTitik
        if(len(convex.list)>1):
            maks = cariTitikMax(convex.list)
            mins = cariTitikMin(convex.list)
            listAtas = []                               #listAtas berisi titik titik yang berada diatas garis maks dan mins
            listBawah = []                              #listBawah berisi titik titik yang berada dibawah garis maks dan mins
            for x in range(0,len(convex.list)):         # Mengiterasi convex.list dan Mengecek apakah titik yang ada berada diatas atau dibawah garis maks dan mins 
                titik = convex.list[x:x+1]
                if((maks[0][0] != titik[0][0] or maks[0][1] != titik[0][1]) and (mins[0][0] != titik[0][0] or mins[0][1] != titik[0][1])):
                    x1,y1,x2,y2,x3,y3 = koordinat(maks,mins,titik)
                    det = determinan(x1,y1,x2,y2,x3,y3)
                    if det>0 :
                        listAtas.append(titik[0])       # JIka determinan lebih dari 0 maka titik tersebut berada di atas garis dan akan dimasukkan ke listAtas
                    elif det<0:
                        listBawah.append(titik[0])      # JIka determinan kurang dari 0 maka titik tersebut berada di bawah garis dan akan dimasukkan ke listBawah
            convex.titikConvex=[]
            if listAtas != [] :
                convex.titikConvex.extend(pecahConvex(listAtas,maks,mins))  # Memanggil fungsi pecahConvex untuk mencari titik Convex Hull
            convex.titikConvex.append(mins[0]) # Menambah titik mins ke titik convex HUll
            if listBawah != [] :
                convex.titikConvex.extend(pecahConvex(listBawah,mins,maks)) # Memanggil fungsi pecahConvex untuk mencari titik Convex Hull
            convex.titikConvex.append(maks[0]) # Menambah titik makss ke titik convex HUll
            convex.simplex()
    def simplex(convex):            # Fungsi simplex  untuk mencari index array titik convex.titikConvex di list convex.list dan memasukkannya ke objek convex.simplices
        koor1=convex.titikConvex[len(convex.titikConvex)-1:len(convex.titikConvex)][0]
        index1 = convex.getIndex(koor1)
        koor2=convex.titikConvex[0:1][0]
        index2 = convex.getIndex(koor2)
        convex.simplices = [[index1,index2]]
        for x in range (0,len(convex.titikConvex)-1):  # Mengiterasi isi list convex.titikConvex
            koor1 = convex.titikConvex[x:x+1][0]
            index1 = convex.getIndex(koor1)
            koor2 = convex.titikConvex[x+1:x+2][0]
            index2 = convex.getIndex(koor2)
            convex.simplices.append([index1,index2])
    def getIndex(convex,koor1):     #Fungsi untuk mencari index array titik convex.titikConvex di list convex.list 
        for x in range(0,len(convex.list)):
            cek = convex.list[x]
            if  cek[0]== koor1[0] and cek[1] == koor1[1] :
                return x


        
