class Human:
    # built-in  - initialize
    def __init__(self,name): #constructor yapısı gibi
        self.name = name
    print("Bir human instance'i üretildi")
    def __str__(self) -> str: #-> str geriye dönüş tipini verir
        return f"STR Fonksiyonundan dönen değer: {self.name}"
    def talk(self, sentence):
        print(f"{self.name}: {sentence}")
        # self.walk  self keywordü fonksiyonlar içerisinde classtaki diğer alanlara erişim sağlar.
    def walk(self):
        print(f"{self.name} is walking..")
