# print('Hello World')
# print('Merhaba')
# print('Merhaba Dünya')
# print('Merhaba Dünya')
# # print('Merhaba Dünya')
# print("Merhaba"+" "+"Şahin")
# print(input("Merhaba, Adın Nedir?"))
# print("Merhaba " + input("Merhaba,Adın Nedir?") + "!")
# print(len(input("ismetMerhaba, Adın Nedir?")))
# name = input("merhaba, adın nedir?")
# print(name)
# name = "İsmet"
# print(name)
# name = "Çiğil"
# print(name)
# isim = input("merhaba,adın nedir?")
# uzunluk = len(isim)
# print(uzunluk)
# ensongidilensehiradi = input("en son hangi şehire gittiniz?")
# evcilhayvanadi = input("evcil hayvanınızın adı nedir?")
# print("Grup Adı: " + " " + ensongidilensehiradi + " " + evcilhayvanadi)
# sayi1 = input("birinci sayıyı giriniz")
# sayi2 = input("ikinci sayıyı giriniz")
# toplam = int(sayi1) + int(sayi2)
# print("toplam = " + str(toplam))
# kisakenar = input("kısa kenarı giriniz: ")
# uzunkenar = input("uzun kenarı giriniz: ")
# cevre = (int(kisakenar) + int(uzunkenar)) * 2
# alan = int(kisakenar) * int(uzunkenar)
# print("dikdörtgenin çevresi: " + str(cevre))
# print("dikdortgenin alanı: " + str(alan))
# print(len(str(433454623932123981)))
# print("ismetcigilbaba"[7])
# print(4523 + 687)
#print(342332_323232_6777)
#print(4.65334)
# print(True)
# ikihanelisayi = str(input("iki haneli sayı gir"))
# toplam = int(ikihanelisayi[0]) + int(ikihanelisayi[1])
# print("toplam: " + str(toplam))
# print(5 * 7 / 3 + 7 -11)
# boy = float(input("boyunuzu giriniz (m): "))
# kilo = float(input("kilonuzu giriniz (kg): "))
# vki = int(kilo/boy*2)
# print("vücut kitle indeksiniz: " + str(vki) )
# yas = input("kac yasındasın")
# yas_int = int(yas)
# ay = yas_int * 12
# hafta = yas_int * 52
# gun = yas_int * 365
# print(f"{ay} aylıksın")
# print(f"{hafta} haftalıksın")
# print(f"{gun} gunluksun")
# print("bahşiş hesaplayıcıya hosgeldın")
# hesap = float(input("hesap kaç tl tuttu"))
# kisisayisi = int(input("kac kisisiniz"))
# oran = float(input("bahşiş oranı ne olsun")
# kisibasi 
# kisibasi = toplam / kisisayisi
# print(f"kişibaşı odemeniz gereken tutar = {kis}")
print("lunaparka hoşgeldiniz")
print("bilet fiyatı yetişkin 10 tl 12 yasından kucuksenız 5tl'dir")
boy = int(input("lütfen boyunuzu giriniz. (cm)"))
yas = int(input("lütfen yaşınızı giriniz."))
biletfiyati = 0
if boy > 80 :
    if(yas < 12):
        biletfiyati = 5
    else:
        biletfiyati = 10
        print(f"çarpışan arabalara binebilirsiniz.Fiyat {biletfiyati} TL")
elif boy > 120 and boy < 140:
    if(yas < 12):
      biletfiyati = 5
    else: 
        biletfiyati = 10
    print(f"lunapark hız trenine binebilirsiniz fiyat {biletfiyati} tl")
elif boy > 120 and boy < 140:
    if(yas < 12):
       biletfiyati = 5
    else:
        biletfiyati = 10
        print(f"gondola binebilirsiniz fiyat {biletfiyati} tl")
elif boy > 140:
    if(yas < 12):
        biletfiyati = 5
    else:
        biletfiyati = 10
        print(f"kamikazeye binebilirsiniz fiyat {biletfiyati} tl")
else:
        print("lunaparkta herhangi bir araca binmek icin boyunuz yetmiyor")