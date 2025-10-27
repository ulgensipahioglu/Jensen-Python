# list ler mutable, yani elemanlari degistirebilirim
 
#liste_adi = [eleman1, eleman2, eleman3,...] koseli paratezle yazilir

ogrenci_1 = 60
ogrenci_2 = 78
ogrenci_3 = 54
ogrenci_4 = 98
ogrenci_5 = 99

notlar  = [60,78,54,98,99]

#variable larla da aynisini yaparim eger daha onceden tanimlandiysa
notlar = [ogrenci_1, ogrenci_2, ogrenci_3, ogrenci_4, ogrenci_5] #ayni sonucu verir

#ilk eleman icin
print(notlar[0]) # 60 verir
#son eleman icin
print(notlar[-1]) #99

#burdan basla sona kadar git
print(notlar[1:]) #[78, 54, 98, 99]

#bastan basla suna kadar git
print(notlar[:3]) #[60, 78, 54]

#tum liste
print(notlar[:]) #[60, 78, 54, 98, 99]

#1den 3e
print(notlar[1:3]) #[78, 54] 1. dahil 3. dahil degil

# normalde fazla index versen patlar ama burda calisiyor
print(notlar[:200]) #[60, 78, 54, 98, 99] hata vermez sonuna kadar gider

#List lerin icinde her seyi tutarsin. int, str, float.. hatta list bile

liste = [[1,2,3],2,4.5,"elma", True]

#ELEMAN DEGISTIME "MUTABLE" oldugu icin elemanlari degistirebilirim
#2. ogrencinin notunu 5 arttir
notlar[1] += 5 #notlar[1] = notlar[1] + 5 
print(notlar[1])

#coklu da degistirebilirim
notlar[0:3] = [10,20,30]
print(notlar)

#eger tek bi elemanla ilk uc elemani degistirmek istersem liste gibi yazmaliyim
notlar[0:3] = [30]
print(notlar) #ilk 3 degeri direkt tek bir 30la degistirdi. sonra kalanini yazdi


#len()
print(len(notlar)) #eleman sayisini verir, virgulle ayrilmislari


#append() liste sonuna 1 eleman eklemek
notlar.append(200) #liste sonuna 200 intini ekler
print(notlar)

notlar.append("elma") #str de ekleniyor
print(notlar)

#extend() liste sonuna 1den fazla eleman eklemek
notlar.extend([100,150,300])
print(notlar)


#insert() listenin belli indexine eleman eklemek ama diger elemanlari kaybetmeden
notlar.insert(0,100) #notlar[0] = 100 ile ayni degil bu eskiyi siliyo ama insert eskiyo de koruyo sadece indexi kayiyo
print(notlar)
notlar.insert(3, 44)
print(notlar)

#remove() listeki istenen elemani sadece siler. (ilk gordugunu siler birden fazlaysa) listede o eleman yoksa hata verir. bu hatayi try except le cozebiliriz
notlar.remove(100)
print(notlar) #ilk gordugunu siler index veremeyiz

#pop() listedeki istenen indexli elemani hem siler hem dondurur
notlar.pop(1) #1.indexteki elemani donurecek listeden de silecek. ayni zaman da pop(1) bir deger de alabilir
print(notlar.pop(1))
a = notlar.pop(1) 
print(notlar)
# eleman sayimdan buyuk sayi yazarsam hata verir


#count listede hangi elemandan kac tane var
notlar.count(30)
print(notlar.count(30))


#Aliasing (takma ad)
#eger bir listetiyi baska listeye esitlersek sonra da birindne bir eleman degistirirsek digerinde de degisir. cunku ayni adresi gosterirler
eski_notlar = notlar
print(eski_notlar)
print(notlar)

notlar.append(88) #88 i bir listeye eklersem digerine de eklenir
print(eski_notlar)
print(notlar)
 
#copy() bunu kullanirsam listemin kopyasi olusur ve baska kutucugun adresini tutar
yeni_notlar = notlar.copy()
print(notlar)
print(yeni_notlar)

notlar.remove(200)
print(notlar)   #sadece notlardan cikti
print(yeni_notlar)

#listelerde Concatenation + ile yapiliyor
print(notlar + yeni_notlar)
liste = notlar + yeni_notlar #yeni degisken tanimlayabilirim
print(notlar)    #listeler degismez kaybolmaz
print(yeni_notlar)
print(liste)

#index() elimdeki elemanin hangi indexte oldugunu soyler
print(notlar.index(100))
#print(notlar.index(9)) #listede olmayan hata verir

#reverse() listeyi tersine cevirir. inpalace olur yani liste artik ters olur.
notlar.reverse()
print(notlar)

#slicing mantigiyla da yapilir terse cevirme ve liste guncellenmez eski haliyle kalir sadece tersine yazdirir. ama istersen ters listeyi bir degiskene atarsin
print(notlar[::-1])
print(notlar)
ters_liste = notlar[::-1]
print(ters_liste)


#sorted. iki sekilde yapiliyor
#sorted() siralar yazdirir orjinal listeyi degistirmez. inplace yapmaz
#print(sorted(notlar)) #hata verdi cunku str int birlikte oldugundan
l = [1,33,2,6,77,9]
print(sorted(l))
print(l) #hala karisik

#.sort() listeyi gunceller. inplace eder
l.sort()
print(l)


#Belirli bir eleman listede veya tuple'da var mı diye in keyword'ü ile sorgu yapabilirim.
l = [1,2,3,4]
print(1 in l) #true doner
print(40 in l) #false doner