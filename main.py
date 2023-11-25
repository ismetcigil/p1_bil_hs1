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
# # print(len(str(433454623932123981)))
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
# print("lunaparka hoşgeldiniz")
# print("bilet fiyatı yetişkin 10 tl 12 yasından kucuksenız 5tl'dir")
# boy = int(input("lütfen boyunuzu giriniz. (cm)"))
# yas = int(input("lütfen yaşınızı giriniz."))
# biletfiyati = 0
# if boy > 80 :
#     if(yas < 12):
#         biletfiyati = 5
#     else:
#         biletfiyati = 10
#         print(f"çarpışan arabalara binebilirsiniz.Fiyat {biletfiyati} TL")
# elif boy > 120 and boy < 140:
#     if(yas < 12):
#       biletfiyati = 5
#     else: 
#         biletfiyati = 10
#     print(f"lunapark hız trenine binebilirsiniz fiyat {biletfiyati} tl")
# elif boy > 120 and boy < 140:
#     if(yas < 12):
#        biletfiyati = 5
#     else:
#         biletfiyati = 10
#         print(f"gondola binebilirsiniz fiyat {biletfiyati} tl")
# elif boy > 140:
#     if(yas < 12):
#         biletfiyati = 5
#     else:
#         biletfiyati = 10
#         print(f"kamikazeye binebilirsiniz fiyat {biletfiyati} tl")
# else:
#         print("lunaparkta herhangi bir araca binmek icin boyunuz yetmiyor")
# sayi = int(input("lütfen tek mi çift mi olduğunu öğrenmek için bir sayı yazınız."))
# kalan = sayi % 2
# if kalan == 0:
#     print("girdiğiniz sayı çifttir")
# else:
#     print("girdiğiniz sayı tektir")
# boy = float(input("boyunuzu giriniz (m): "))
# kilo = float(input("kilonuzu giriniz (kg): "))

# vki = int(kilo/boy**2)
# if vki < 18.5:
#     print(f"vücut kitle indeksiniz: {vki} , zayıfsınız")
# elif vki > 18.5 and vki < 25:
#     print(f"vücut kitle indeksiniz: {vki} , kilonuz normal")
# elif vki > 25 and vki < 30:
#     print(f"vücut kitle indeksiniz: {vki} , kilolusunuz")
# elif vki > 30 and vki < 35:
#     print(f"vücut kitle indeksiniz: {vki} , obezsiniz")
# elif vki > 35:
#     print(f"vücut kitle indeksiniz: {vki} , aşırı kilolusunuz")
# yil = int(input("hangi yılı kontrol etmek istiyorsun?"))
# if yil % 4 == 0:
#     if yil %100 == 0:
#         if yil %400 == 0:
#             print(f"{yil} artık ir yıldır.")
#         else:
#             print(f"{yil} artık bir yıl değildir.")
#     else:
#         print(f"{yil} artık bir yıl değildir.")
# else:
#     print(f"{yil} artık bir yıl değildir.")
# boy = input("cemil kerem pizzaya hoşgeldiniz. hangi boy pizza istersiniz? K veya O veya B =>")
# ekstrasos =input("ekstra sos ister misiniz? E veya H =>")
# ekstrapeynir = input("ekstra peynir ister misiniz? E veya H =>")
# toplam = 0
# if boy == "K":
#     toplam += 15
# elif boy == "O":
#     toplam += 20
# elif boy == "B":
#     toplam += 25

#     if ekstrasos == "E":
#         if boy == "K":
#             toplam += 2
#         else:
#             toplam += 5
#             if ekstrapeynir == "E":
#                 toplam += 3
# print(f"Toplam Ödeme = {toplam}")
# print("sevgi hesaplamaya hoşgelşdiniz")
# isim1 = input("adınız nedir")
# isim2 = input("onun adı nedir")

# isimler = ( isim1 + isim2 ).lower()

# g = isimler.count("g")
# e = isimler.count("e")
# r = isimler.count("r")
# ç = isimler.count("ç")
# e = isimler.count("e")
# a = isimler.count("a")
# ş = isimler.count("ş")
# k = isimler.count("k")

# toplam = g + e + r + ç + e + k + a + ş + k

# if( toplam < 10 and toplam > 90):
#     print(f"Sevgi Puanınız: {toplam}, berk ve enez zalim gibisiniz") 
# elif( toplam > 40 and toplam < 50):
#     print(f"Sevgi Puanınız: {toplam}, SÜPERSİNİZ!")
# else:
#     print(f"Sevgi Puanınız: {toplam}") 
# import random

# randomsayı = random.randint(1,3)
# cevap = int(input("taş (1), kağıt (2), makas (3) seçiniz"))
# import random

# randomSayi = random.randint(1,3)
# cevap = int(input("Taş (1), Kağıt (2) Makas (3) Seçiniz"))
#       _.-.._         _._
#                              _,/^^,y./  ^^^^"""^^\= \
#                              \y###XX;/  /     \    ^\^\
#                                `\Y^   /   .-==||==-.)^^
#            ,.-=""""=-.__       /^ (  (   -/<0>++<0>(
#          .^      .: . . :^===(^ \ (  (  /```^^^^^^^)
#         /      .: .,GGGGp,_ .(   \   /    /-(o'~'o))
#       .^      : . gGG"""YGG}. \   )   / /  _/-====-\
#      /       (. .gGP  __ ~~ . .\  \  (    (  _.---._)
#     /        (. (GGb,,)GGp. . . \_-^-.__(_ /______./
#    (          \ . `"!GGP^ . . . . ^=-._--_--^^^^^~)
#    (        /^^^\_. . . . . . . . . . . . . . . . )
#    )       /     /._. . . . . . . . . . . . . ._.=)
#    \      /      |  ^"=.. . . . . . . ._++""\"^    \
#     \    |       |       )^|^^~'---'~^^      \     )
#     )   /        )      /   \                 \    \
#     |`  |        \     /\    \                (    /
#     |   |         (   (  \ . .\               |   (
#     )   |         )   )   ^^^^^^              |   |
#    /. . \         |  '|                       )   (
#    ^^^^^^         )    \                      /. . \
#                   / . . \                     ^^^^^^
#                   ^^^^^^^
# yas = int(input("kaç yaşındasınız"))
# if yas >= 18:
#     saglik = input("sağlıklı mısın? e veya h =>")
#     if saglik == "e":
#         print("ehliyet alabilirsin")
#     else:
#         print("ehliyet alamazsın")
# else:
#    print("ehliyet alamazsın")
# sifre = "005162"
# print("cemo kero bankaya hosgeldın")
# sifregirilen = input("lütfen şifre giriniz")
# if len(sifregirilen) != 6:
#     print("eksik ya da fazla tuşladınız")
# elif sifre == sifregirilen:
#     print("yüce cemo kero sizi karşılıyor")
# else:
#     print("yanlış şifre :D")
# import math
# boy = float(input("boyunuzu metre cinsinden giriniz"))
# kilo = int(input(" kilonuzu kg cinsinden giriniz"))

# idealkilo = math.floor(22*boy*boy)
# fark = abs(idealkilo-kilo)
# if idealkilo > kilo:
#     print(f"{fark} kilo almalısın")
# else:
#     print(f"{fark} kilo vermelisiniz
# sehirler  = [
#     "Adana","Adıyaman","Afyonkarahisar","Ağrı","Aksaray","Amasya","Ankara","Antalya","Ardahan","Artvin","Aydın","Balıkesir","Bartın","Batman",
# "Bayburt","Bilecik","Bingöl","Bitlis","Bolu","Burdur","Bursa","Çanakkale","Çankırı","Çorum","Denizli","Diyarbakır","Düzce","Edirne","Elazığ",
# "Erzincan","Erzurum","Eskişehir","Gaziantep","Giresun","Gümüşhane","Hakkari","Hatay","Iğdır","Isparta","İstanbul","İzmir","Kahramanmaraş","Karabük",
# "Karaman","Kars","Kastamonu","Kayseri","Kilis","Kırıkkale","Kırklareli","Kırşehir","Kocaeli","Konya","Kütahya",
# "Malatya","Manisa","Mardin","Mersin","Muğla","Muş","Nevşehir","Niğde","Ordu","Osmaniye","Rize","Sakarya","Samsun","Şanlıurfa",
# "Siirt","Sinop","Şırnak","Sivas","Tekirdağ","Tokat","Trabzon","Tunceli","Uşak","Van","Yalova","Yozgat","Zonguldak"
# ]
# print(sehirler[0])
# print(sehirler.index("Adana"))
# print(sehirler[12])
# print(sehirler[80])
# print(sehirler[-1])
# print(sehirler[-2])
# sehirler[33] = "İçel"
# print(sehirler[33])

# sehirler.append("Tarsus")
# print(sehirler[81])
# print(len(sehirler))
# sehirler.remove("Tarsus")
# print(len(sehirler))
# sehirler.pop()
# print(len(sehirler))
# import random
# isimler = "İsmet, Soner, Cagan, Berk, Cemosit, Cakır"
# isimdizisi = isimler.split(", ")
# index = random.randint(0, len(isimdizisi) - 1)
# print(f"hesabı {isimdizisi[index]} ödeyecek")
# row1 = ['⬜️', '⬜️', '⬜️']
# row2 = ['⬜️', '⬜️', '⬜️']
# row3 = ['⬜️', '⬜️', '⬜️']
# harita = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}\n")

# pozisyon = input("hazineyi nereye koymak istersiniz\n")

# yatay = int(pozisyon[0]) - 1
# dikey = int(pozisyon[1]) - 1 
# harita[dikey][yatay] = "X"
# print(f"{row1}\n{row2}\n{row3}\n")
# row1 = ['⬜️', '⬜️', '⬜️']
# row2 = ['⬜️', '⬜️', '⬜️']
# row3 = ['⬜️', '⬜️', '⬜️']
# harita = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}\n")

# pozisyon = input("Hazineyi nereye koymak istersin?\n")

# yatay = int(pozisyon[0]) -1
# dikey = int(pozisyon[1]) - 1 
# harita[dikey][yatay] = "X"
# print(f"{row1}\n{row2}\n{row3}\n")
# import random
# taş = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''

# kağıt = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''

# makas = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# while True:
#     kullaniciSecimi = int(input("Taş(0), Kağıt(1), Makas(2) Seç!"))
#     bilgisayarsecimi = random.randint(0,2)

#     print("senin seçimin")
#     if kullaniciSecimi == 0:
#         print(taş)
#     elif kullaniciSecimi == 0:
#         print(kağıt)
#     elif kullaniciSecimi == 2:
#         print(makas)

#     print("bilgisayarın seçimi")
#     if bilgisayarsecimi == 0:
#         print(taş)
#     elif bilgisayarsecimi == 1:
#         print(kağıt)
#     elif bilgisayarsecimi == 2:
#         print(makas)



#         if kullaniciSecimi >=3 or kullaniciSecimi < 0:
#             print("0 , 1 ,veya 2 giriniz!")
#         elif kullaniciSecimi == 0 and bilgisayarsecimi == 2:
#             print("Kazandın!")
#         elif bilgisayarsecimi == 0 and kullaniciSecimi == 2:
#             print("Kaybettin")
#         elif kullaniciSecimi > bilgisayarsecimi:
#             print("Kazandın!")
#         elif bilgisayarsecimi > kullaniciSecimi:
#             print("Kaybettin!")
#         else:
#             print("Berabere!")
# meyveler = ["Elma", "Armut","Şeftali"]
# for meyve in meyveler:
#     print(meyve)
# for sayi in range(0,100):
#     if (sayi%3) == 0 and  (sayi%5)==0:
#         print(sayi)
# girilensayi = int(input("bir sayı giriniz"))

# carpim = 1

# for sayi in range(1, girilensayi+1):
#     carpim *= sayi

# print(f"girdiğin sayının faktöriyeli : {carpim}")
# for sayi in range(0,10):
#     print(f"8 x {sayi} = {8 * sayi }")
# for sayi in range(0,100):
#     if (sayi%2) == 0 and  (sayi%3)==0:
#         print(sayi)
# boylar = input("öğrenci boylarını cm cinsinden aralarında bir boşluk olacak şekilde giriniz")
# boydizisi = boylar.split(" ")
# toplam = 0
# for boy in boydizisi:
#     toplam += int(boy)

# print(f"girilen boyların ortalaması : {toplam / len(boydizisi)}")
# puanlar = input("öğrenci puanlarını arada boşluk olacak şekilde giriniz")
# enyüksekpuan = int(puanlar.split(" ")[0])
# for puan in puanlar.split(" "):
#     if enyüksekpuan < int(puan):
#         enyüksekpuan = int(puan)

# print(f"En yüksek puan : {enyüksekpuan}")
# print(f"En küçük puan : {min(puanlar.split(' '))}")
# def fonksiyonum() :
#     print("Merhaba")
#     print("Dünya")
# fonksiyonum()