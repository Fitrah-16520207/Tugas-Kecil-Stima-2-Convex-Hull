from MainConvexHull import *
from MathConvexHull import *

def getTitik(listBagi,maks,mins): # Fungsi untuk mencari titik-titik yang berada di atas atau di luar garis maks dan mins
    list = []
    for x in range(0,len(listBagi)) :
        titik = listBagi[x:x+1]
        if((maks[0][0] != titik[0][0] or maks[0][1] != titik[0][1]) and  (mins[0][0] != titik[0][0] or mins[0][1] != titik[0][1])):
            x1,y1,x2,y2,x3,y3 = koordinat(maks,mins,titik)
            det = determinan(x1,y1,x2,y2,x3,y3)
            if det>0 :                          # Jika det lebih dari 0 maka titik tersebut berada di luar garis maks dan mins
                list.append(titik[0])
    return list

def pecahConvex(listBagi,maks,mins): # Fungsi untuk mencari titk terjauh dari garis maks dan mins dan membagi dua list
    if(len(listBagi)>1):        # Jika listBagi (list titik-titik) berjumlah lebih dari satu
        titikTengah = mins
        JarakMax = 0
        for x in range(0,len(listBagi)) : # Mencari titik terjauh
            titik = listBagi[x:x+1]
            if((maks[0][0] != titik[0][0] or maks[0][1] != titik[0][1]) and  (mins[0][0] != titik[0][0] or mins[0][1] != titik[0][1] )):
                x1,y1,x2,y2,x3,y3 = koordinat(mins,maks,titik)
                jarak = jarakTitik(x1,y1,x2,y2,x3,y3)
                if(jarak>JarakMax):
                    JarakMax = jarak
                    titikTengah = titik
        listKanan = getTitik(listBagi,maks,titikTengah) # listKanan berisi titik-titik yang berada diatas garis titikTengah (titik terjauh) dan titik maks
        listKiri = getTitik(listBagi,titikTengah,mins) # listKiri berisi titik-titik yang berada diatas garis titik mins dan titikTengah (titik terjauh)
        if listKanan != [] :
            listConvex=pecahConvex(listKanan,maks,titikTengah)
            listConvex.extend(titikTengah)
        else :
            listConvex = titikTengah                    # Menambah titikTengah atau terjauh dalam list yang berisi titik Convex Hull
        if listKiri != []:
            listConvex.extend(pecahConvex(listKiri,titikTengah,mins))

        return listConvex
    elif listBagi == []: # Jika listBagi kosong
        return 
    else : # Jika listBagi berisi satu 
        titik = listBagi[0:1]
        x1,y1,x2,y2,x3,y3 = koordinat(maks,mins,titik)  
        if determinan(x1,y1,x2,y2,x3,y3) > 0:  # Mengecek apakah titik terakhir berada diatas garis maksimal dan minimal
            return titik  # Jika iya maka titik tersebut termasuk titik Convex Hull
        else :
            return
