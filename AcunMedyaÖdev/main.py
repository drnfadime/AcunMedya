print("Kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)

baslik = "İhtiyaç Kredisi"
print(baslik)

vade = 36   #numerik ifade
ekVade = 6
vade2 ="36" #metinsel ifade

#float, double, decimal  
aylikOdeme = 200.50

#boolean => True veya False
yukselisteMi = False

#matematiksel operatörler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)
print(36 + 6)

# - 
print(5 -5)
print(vade - 12)
print(vade - ekVade)
print(36 - 6)

# *
print(5*5)
print(vade * 2)
print(vade * ekVade)
print(10*10)

# /
print(5/5)
print(vade / 2)
print(vade / ekVade)
print(10/2)


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# % => mod operatör
print(10%2)
print(vade % 5)
print(vade % ekVade)
print(30 % 10)


# mantıksal operatörler
print(1 == 1)
print(1 == 2)

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(3 < 1)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

# or and 
print(1 < 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2) 

print(2 > 1 or 1 > 2 and 3 > 2) 

# karar yapıları
# if else

sayi1 = 10
sayi2 = 15
if sayi1 < sayi2:
    print("Sayi1 Sayi2' den küçüktür.")
elif sayi1 == sayi2:
    print("İki sayı eşittir.")
else:
    print("Sayi1 Sayi2'den büyüktür. ")

print("Burası if bloğunun dışıdır.")



    






 