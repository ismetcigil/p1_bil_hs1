#0-100 arasındaki çift sayıların toplamını ekrana yazan yazılm
toplam = 0
for a in range(101):
    if a % 2 == 0 :
        toplam = toplam + a
print(toplam)
        