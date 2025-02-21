# alias
import matematik as m # takma ad dosyaya özel
from day2 import sayHello  #dosyadaki sadece belli kısımları import etmek 
from human import Human
#built-in modules
import random
from selenium import webdriver 
#package

print(m.topla(10,20))

print(random.randint(0,100)) #0-100 (dahil) arası rastgele sayı 

human1 = Human("Mirza")
human1.talk("Merhaba")

chromeDriver = webdriver.Chrome()
# packages
