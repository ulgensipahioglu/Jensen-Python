# Setler
#kumeler gibidir. uniqe degerleri tutarlar. 
'''
Sadece özgün değerleri tutan, içerisinde bir eleman var mı yok mu, başka bir setle hangi elemanları farklı gibi işlemleri performanslı bir şekilde yapabileceğimiz bir veri yapısıdır.

Dictionary'ler gibi eleman sorgusu yapmak hızlıdır. Dictionarylerde key-value çift olarak bulunduğu için aynı uzunluktaki bir setten daha fazla yer kaplar.

Setler indexlenemez.

Setler mutable'dır.'''
s = {1,2,3,4.}
s1 = set() #bos set
print(type(s1))
dic = {} #bos dictionary dictionary le parantexleri ayni ama bos set icin set() yaz
print(type(dic)) 

l = ("a","b","c","a", "b", "c")
s2 = set(l) #l tapilindan bir sey olusturur. Ayni elemani 1 kere yazar
print(s2)

l2 = [1,2,3,4,1,2,3,4]
s3 = set(l2) #l2 lstinden bir set olusturur. Ayni elemani 1 kere yazar
print(s3)

#strinlerden de set olusturulur. 
mesaj = "Merhaba, Dunya!"
l4 = set(mesaj) #mesaj degiskeninin elemanlariyla bana bir set olustur
print(l4) 
print(type(l4))
print(mesaj)
print(type(mesaj))

# cikti boyle olur {'b', ' ', 'D', 'e', 'h', ',', 'y', 'M', '!', 'u', 'r', 'a', 'n'}
#boslukalri da karakter sayar, sirali degildir her seferinde baska sirayala cikabilir.
#INDEXLENEMEZ karisiktir elema siralamasi

print("e" in l4) # e elemani l4 set inin icinde mi?
#True

# len() setin eleman sayisini aliriz
print(len(l4)) #13

#.add() ile elaman eklerim
s = {1,2,3,4}
s.add(6)
print(s)
# zaten olan bi elemani eklemek istersem hata almam ama eklemez

#.remove ile elaman silerim
s.remove(6)
print(s)
#olmayan elemani silmeye calissam HATA alirim

#.discard() ile yoksa ERROR verme varsa SIL yaparim
s.discard(9)
print(s)

#.difference() (fark)
s1 = set([1,5,10])
s2 = set([2,5,3])
# s1 in hangi elemanları s2 den farklıdır.
print(s1.difference(s2)) #bunu ile
print(s1 - s2) #bu ayni sonucu verir

#.symmetric_difference() s1'in s2 den farkı ile s2'nin s1 den farkının birleşimi. (s1 \ s2) U (s2 \ s1) - > s1 U s2 - (s1 n s2)
#yani ortak eleman haric elemanlar
s1 = set([1,5,10])
s2 = set([2,5,3])
# (s1 \ s2) U (s2 \ s1)  - > A U B - (A n B)
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1)) #ayni sonucu aliriz

#.intersection() kesisim
s1 = set([1,5,10])
s2 = set([2,5,3])
print(s1.intersection(s2))
print(s2.intersection(s1)) #ayni sonucu aliriz
# `&` operatörü setlere uygulanınca kesişim olur
print(s1 & s2)

# .intersection_update() kesişim yapıp s1 in değerini buna günceller
s1.intersection_update(s2) # s1 = s1.intersection(s2) islemini yapmis olur aslinda
print(s1) #s1 su an kesisimle ayni oldu

#.union() birlesim. tum elemanlar
s1 = set([1,5,10])
s2 = set([2,5,3])
print(s1.union(s2))

#.isdisjoint() s1 ∩ s2 = Ø (null) olup olmadığını kontrol eder. Bolean sonuc doner
s1 = set([1,5,10])
s2 = set([2,5,3])
s3 = set([11,12])
print(s1.isdisjoint(s2)) # s1 ∩ s2 ≠ Ø(boş küme) değil, o yüzden False döner

print(s1.isdisjoint(s3)) # s1 ∩ s2 ≠ Ø(boş küme) o yüzden True döner
#aslinda bunu kontrol eder
len(s1.intersection(s2)) == 0 #kesisimleri o elemanli mi?

#.issubset() s1.issubset(s2), s1'in s2'nin alt kümesi olup olmadığını kontrol eder. Bolean sonuc doner
s1 = set([1,5,10])
s2 = set([2,5,3])
print(s1.issubset(s2)) #s1 s2 nin alt kumesi degil cunku farkli elemanlari var False doner
s3 = set([2,5])
print(s3.issubset(s2)) #s3 s2nin elemanlarindan olusuyo farkli elemani yok o yuzden True doner.

#.issuperset() s2.issuperset(s3) s2'nin s3'ün üst kümesi olup olmadığını sorgular
s1 = set([1,5,10])
s2 = set([2,5,3])
s3 = set([2,5])
print(s2.issuperset(s3)) #s3 s2nin elemanlarinda olusmus. s2 daha buyuk ama icinde s3 un tum elemanli var
