import numpy as np
liste=[[1,10,3],[4,5,16],[27,58,9]]
matris=np.matrix(data=liste,dtype="uint8")
transpoze=matris.transpose()
det=np.linalg.det(matris)
yeniMatris=matris*2
print(matris)
print(transpoze)
print(det)
print(yeniMatris)

dizi=np.linspace(1,50,10)
ort=dizi.mean()
std=dizi.std()
print(dizi[dizi>25])
print(dizi)
print(ort)
print(std)
for i in dizi:
    karesi=i*i
    print(karesi)

yeniDizi=np.linspace(0,360,100)
print(yeniDizi)
for i in yeniDizi:
    radyan=np.deg2rad(i)
    sin_val=np.sin(radyan)
    cos_val=np.cos(radyan)
    print("Sinüsü:",sin_val)
    print("Cosu:",cos_val)
