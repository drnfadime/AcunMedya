from human import Human


faiz = 1.59
vade = "36"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))


print(int(vade)+12)  # type conversion
# print(int(krediAdi)) 
faiz = str(faiz)
print(type(faiz))

vade = 36 #int(input("Lütfen istediğiniz vade sayısını giriniz: "))
print(type(vade))
vade = vade + 12

# string interpolation
# Seçtiğiniz vade sonucu ortaya çıkan vade: 
print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi=vade)) #format fonksiyonu
print(f"Seçtiğiniz vade sonucu ortaya çıkan vade: {vade}") #f-string

isim = "Halit" #input("İsminizi giriniz:")
metin = "Merhaba {name}".format(name="Samet")
print(metin)


# f-string
metin = f"Hoşgeldiniz {isim}" #parantez içine python kodu da yazılabilir.
print(metin)


#listeler
#döngüler
#fonksiyonlar

dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
print(type(krediler))

print(krediler[0])

print(len(krediler)) #length
# print(krediler[3]) => hata verir

krediler.append("Özel Kredi") #Liste sonuna eleman ekler.
print(krediler)

krediler.append("X Kredisi")
print(krediler)

krediler.pop(0) #Listeden eleman siler.
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

#remove index yerine değer bazlı çalışır
krediler.remove("Taşıt Kredisi") #bulduğu ilk elemanı siler.
print(krediler)

krediler.extend(["Y Kredisi", "Z Kredisi"])
print(krediler)

# for
x = 10 # range içerisine dışarıdan değer verilebilir.
for i in range(x): 
    print(i)
print("*************")

for i in range(5,10):
    print(i)
print("*************")

for i in range(0,51,10):
    print(i)
print("*************")

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]
for kredi in krediler :
    print(kredi)
print("*************")
for i in range(len(krediler)):
    print(krediler[i])
print("*************")


# sonsuz döngü
i = 0
while i < 10:
    print("x")
    i +=1
print("y")

print("*************")

while True:
    print("x")
    break

print("*************")

i = 0
while i < len(krediler):
    print(krediler[i])
    i+=1
    if krediler[i] == "Konut Kredisi":
        break

# fonksiyonlar

fiyat = 100
indirim = 20

def calculate():
    print(100-20)

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(name):
    print(f"Merhaba {name}")

calculate()
calculateWithParams(50,10)
sayHello("Arif")


def calculateAndReturn(fiyat,indirim):
    return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)


# sınıflar => classlar
# modules
# paket yönetimi


# instance => örnek 
human1 = Human("Enes")
human1.talk("Merhaba")
human1.walk()
print(human1)


human2 = Human("Halit")
human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba") # tek satırda değişken atamadan yapılabilri



