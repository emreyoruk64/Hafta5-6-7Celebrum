toplama='+'
cikarma='-'
carpma='*'
bolme='/'
a=int(input("Lutfen 1. sayiyi giriniz:"))
b=int(input("Lutfen 2. sayiyi giriniz:"))
x=input("Lutfen yapacaginiz islemi seciniz:")
if(x=='+'):
    print("Sonuc:" , (a+b))
elif(x=='-'):
    print("Sonuc:" , (a-b))
elif(x=='*'):
    print("Sonuc:" , (a*b))
elif(x=='/'):
    print("Sonuc:" , (a/b))
else:
    print("Lutfen gecerli bir islem girin!")

# Tür dönüşümü
sayi="5"
sayi1=int(sayi)
print(sayi1)

sayi1=10
sayi2=float(sayi1)
print(sayi2)

sayi3=11
stringSayi=str(sayi3)
print(stringSayi)

