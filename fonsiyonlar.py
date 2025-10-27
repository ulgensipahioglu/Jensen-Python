#Fonksiyonlar

#def fonksiyonun_adı(input):

def fonksiyon(x): #def kelimesi bir fonksiyon olusturuyorum demek.
          #f fonksiyonun adi, x de degisken
    
    res = x * x
    
    if x % 2 == 0: #icinde if for kullanabilirim
        
        return res  #return yazmazsam sonuc donmez 
    else:
        return res + 10
    
    print("Square of " + str(x) + ": " + str(res)) #returnden sonrakiler islevsizdir, calismaz
    
print(fonksiyon(10))


def f(x): 
    res = x * x 
    for i in range(10): 
        res += 20
        return ("hey")
    
print(f(13))

def f(x):  #liste olusturma fonksiyonu yazalim
    
    l = []  #bos liste olustur
    res = x * x  #yapilcak islemler buraya
    for i in range(10): #for dongusu basladi. range 10 kadar i dondur 
        res += 20 #20 ekle
        l.append(res) #l listesine ekle
    return l #l yi dondur

print(f(10))
#[120, 140, 160, 180, 200, 220, 240, 260, 280, 300]
