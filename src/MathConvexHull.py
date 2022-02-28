def koordinat(maks,mins,titik): # Fungsi untuk mengasign nilai x1,y1,x2,y2,x3,y3 dari titik maks,mins, dan "titik"
    x1 = mins[0][0]
    x2 = maks[0][0]
    x3 = titik[0][0]
    y1 = mins[0][1]
    y2 = maks[0][1]
    y3 = titik[0][1]
    return x1,y1,x2,y2,x3,y3

def cariTitikMax(list): # Fungsi untuk mencari titik dengan absis maksimal
    titikMax = list[0:1]
    maks = 0
    for x in range(0,len(list)) :
        titik = list[x:x+1]
        x1 = titik[0][0]
        if (maks < x1):
            maks = x1
            titikMax = titik
    return titikMax

def cariTitikMin(list): # Fungsi untuk mencari titik dengan absis minimal
    titikMin = list[0:1]
    mins = 99999
    for x in range(0,len(list)) :
        titik = list[x:x+1]
        x1 = titik[0][0]
        if (mins > x1):
            mins = x1
            titikMin = titik
    return titikMin

def jarakTitik(x1,y1,x2,y2,x3,y3): # Fungsi untuk mencari jarak terdekat dari suatu titik (x3,y3) ke garis (x1,y1) dan (x2,y2)
    a = (y2-y1)/(x2-x1)
    b = -1
    c =  a  *(-x1) + y1
    return abs((a*x3+b*y3+c)/(a*a +b*b))

def determinan(x1,y1,x2,y2,x3,y3): # Fungsi untuk mencari nilai determinan dari titik x1,y1,x2,y2,x3,y3
    return x1*y2+ x3*y1+x2*y3 - x3*y2 - x2*y1 - x1*y3

def jarakDuaTitik(x1,y1,x2,y2):                         # Mengecek jarak antara dua titik 
    return (x1-x2) * (x1-x2) + (y1-y2) * (y1-y2)