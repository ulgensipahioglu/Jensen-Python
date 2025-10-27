#Non-scalar Veri Tiplerinde For 
'''
for döngüsünü işlerken for <değişken> in <obje> yapısında, her iterasyonda değişkenin tek tek objenin elemanlarına eşit olduğunu konuşmuştuk.

list, tuple, dictionary non-scalar veri tiplerini gördük ve bunların hepsinin içsel bir yapısı var, şimdi bunların elemanlarında for kullanarak iterasyon yapmaya bakalım.'''
#Listelerde İterasyon
notlar = [90, 72, 81,77] #ogrenci notlari listesi
for e in notlar:
    print(e) #notlari sirayla yazdirir
print(notlar[:])

#sinif not ortalamsi
t = 0                   #sifirdan baslattim
for e in notlar:        #e tum notlar elemanlarini gezip o elemanin degerini alacak
    t += e              #t=0 ve e her iterasyonda t'ye eklenerek tum elemanlari topluyor
ortalama = t / len(notlar) #for bittiginde yani tum elemanlari gezdiginde,  t tum elemanlarin degerleinin toplami
print(ortalama)         #toplami da notlarin eleman uzunluguna (sayisina) bolunce ort bulunur

#Bunun aynısını range() fonksiyonu ile de yapabilirdik. 
'''
range() ile indexlerde iterasyon yapıp indexing ile değerlerine de ulaşabilirdim. 
(Range belirli bir listenin indexlerinde iterasyon yapmamı sağlamıyor, 
range(len(notlar)) diyince bize 0,1,2.. len(notlar)-1 sayılarını verecek, 
bunlar da listenin indexleriyle örtüşüyor, yoksa range() index verir diye bir şey yok.)'''

for i in range(4):
    print("Iteration: ", i) #index sifirdan baslar sonuncu dahil degildir. "0,1,2,3"

#ama istedigim indexten baslayabilirim
for i in range(2,4):
    print("Iteration: ", i) #"2,3"

#ortalam hesabi
notlar = [90, 72, 81,77]
t = 0

for i in range(len(notlar)): #notlar listesinin uzunlugu kadar index
    t += notlar[i] #t her seferinde notlar listesinin indexlerinin degerini alir
    
ortalama = t / len(notlar)

print("Ortalama:",ortalama)


#range() ile indexing yontemiyle yapiyoruz ve bu sekilde listemiz de degisiyor.
#diyelim ki notlara 10 puan daha eklicem. bunu ilk yontemle yapamam o sadece anlik ekler listeyi degistirmez

notlar = [90, 72, 81, 77]
for e in notlar:
    print(e) #bu e sadece degerlerdir
    
for e in notlar:
    print(e)
    e = e + 10 #10 ekledim
    print(e) #yazdirdim
    print(notlar) #listeyi tekrar yazdirdigimda notlar degismez
    print("--------------")

print(notlar) #listeyi tekrar yazdirdigimda notlar degismez

#range() degistirir. Güncelleme mantığını range() ile indexlerinde iterasyon yaparak yapacağım.
 
for i in range(len(notlar)): #notlar index uzunlugu kadar iterasyon gez
    notlar[i] += 10          #her index e 10 ekle
    print(notlar[i])         
print(notlar)                 #tum liste yenilendi


#1. siradaki ogrenci haric digerlerini 5 puan ekle
#continue

for i in range(len(notlar)):
    
    if i == 0:
        continue  #0. index yani ilk eleman ici atla
    
    notlar[i] += 5

print(notlar)

#break
'''
Diyelim ki bir listenin içinde belirli bir eleman var mı diye kontrol etmek istiyoruz. 
Bulunca aramaya devam etmeyeceğim. Devam etme mantığını break ile sağlayacağım.
İlk kullanıcıya hangi sayıyı aradığını soracağız, 
sonra bu sayı var mı kontrol edeceğiz.
'''

"""x = int(input("Hangi sayiyi kontrol edeyim?:"))
l = [2,3,40,100,10,1]

for e in l:
    print(e) #iterasyon break ile çıkmış mı görelim mi diye
    if e == x:
        print("Buldum!")
        break
else:
    print("Listede yok.")"""

#Tuple'lerda İterasyon
#eleman degisikligi haric listelerle ayni

t = (1,2,3,4)

for e in t:
    print(e)
    
#range()
for i in range(len(t)):  #range ile yazdirabilirim
    print(t[i])
    
toplam = 0
for i in t:
    toplam += i
print(toplam)

#range()
z = 0
for j in range(len(t)): #range() ile toplan ya da ort bulabilrim
    z += t[j]
print(z)


for i in t:
    i += 10  #bu sekilde 10 ekleyebilim. ama sadece eklenmis sayilari yansitir. tupilin icindeki degerleri degistirmez
    print(i)
print(t)

#ama indexlerde degisikliklik yapamam, yani range() kulanamam
#for i in range(len(t)):
 #   t[i] += 2  #hata verir


#Dictionary'lerde İterasyon
'''
Burada durum biraz farklı. Default olarak elemanlarında dolaş diyince key 'lerde iterasyon yapıyor. 
Zaten index mantığı olmadığı için range() ile yapmak çoğu zaman karşımıza çıkmaz.'''

d = {"student_1": [90,89], "student_2": [80,83], "student_3": [72,71]}

for k in d:
    print(k) #keyleri gezer ve onlari yazar. degerleri degil
    
#degerleri istiyorsam

for k in d:
    v = d[k] #d[k] bununla dictionay nin icindeki degeri aliyorduk. burda da o degeri v degiskenine atayip v yi yazdirdik
    print(v) #bu sekilde sadece degerleri aldik


#Veya d.values() diyerek value'lerında iterasyon yapabilirim.

d = {"student_1": 90, "student_2": 80, "student_3": 72}
for v in d.values():
    print(v)

d = {"student_1": [90,89], "student_2": [80,83], "student_3": [72,71]}
for v in d.values():
    print(v)
    
    
#85'den fazla alan biri var mı diye bakmak istiyorum diyelim, 
# ve bunun kim olduğunu (olduklarını) bulmak istiyorum.

d = {"student_1": 90, "student_2": 80, "student_3": 72}
for k in d:
    value = d[k]
    
    if value > 85:
        print(k)
        
        
#Aynı anda hem key hem de value'larda iterasyon yapmak için:

for k,v in d.items():
    print("key değeri:", k, "value değeri:", v)