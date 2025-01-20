import random
rastgele=random.randint(1,10)

while True:
    sayi=int(input("Lutfen 1 ile 10 arasında bir sayi girin:"))
    
    if rastgele>sayi:
        print("Yazdiginiz sayi secilen sayidan kucuk")
        continue
    elif rastgele<sayi:
        print("Yazdıgınız sayi secilen sayidan buyuk") 
        continue
    elif sayi==rastgele:
        print("Tebrikler, secilen sayiyi buldunuz")
        break
   
        


