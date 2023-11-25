harclik = int(input("Harçlığınızı giriniz."))
enflasyon = int(input("Enflasyon oranını giriniz"))
yeniharclik = harclik * enflasyon / 100 + harclik
print("Yeni harçlığınız ektedir:" , yeniharclik)