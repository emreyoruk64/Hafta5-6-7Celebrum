import random

def amiral_batti():
    print("Amiral Battı Oyununa Hoş Geldiniz!")
    print("5x5 bir tahtada geminin yerini bulmaya çalışın.")

    # Gemi koordinatını rastgele belirle
    gemi_satir = random.randint(1, 5)
    gemi_sutun = random.randint(1, 5)

    # Kullanıcıya 5 tahmin hakkı ver
    tahmin_hakki = 5

    while tahmin_hakki > 0:
        print(f"Kalan tahmin hakkınız: {tahmin_hakki}")

        try:
            satir = int(input("Satır seçin (1-5): "))
            sutun = int(input("Sütun seçin (1-5): "))

            if satir < 1 or satir > 5 or sutun < 1 or sutun > 5:
                print("Lütfen 1 ile 5 arasında bir değer girin.")
                continue

            if satir == gemi_satir and sutun == gemi_sutun:
                print("Tebrikler, gemiyi vurdunuz!")
                break
            else:
                print("Yanlış tahmin, tekrar deneyin!")

            tahmin_hakki -= 1

        except ValueError:
            print("Lütfen geçerli bir sayı girin.")

    if tahmin_hakki == 0:
        print("Tahmin hakkınız bitti. Oyunu kaybettiniz!")
        print(f"Gemi ({gemi_satir}, {gemi_sutun}) koordinatındaydı.")

# Oyunu çalıştır
amiral_batti()