#Enumerate-Zip
#Variable Unpacking sayesinde for ile non-scalar yapılar içerisinde dolaşırken 
#eleman ve index uzerinde ayni anda dolasabilriz

#aynisi iterasyonla da yapilir ama unpacking daha kisa
l = [(1,2), (10,20)]
for e in l: #e l nin elemanlari
    print(e)
    
for e in l: #e l nin elemanlari
    a, b = e #e su an iki karaktere sahip. a ve b yi o ikisine esiyler
    print(a)
    print(b)
    print("*********")
    
#su sekilde direkt de deger atayabilrim
for a, b in l: #a ve b direk olarak l nin elemanlarina esitlenir. tek tek
    print("tuple'ın ilk elemanı", a)
    print("tuple'ın ikinci elemanı", b)
    print("-----------------------------")
    
#enumerate() bize (index, element) olarak verecek.
adlar = ['Tyler', 'Blake', 'Cory', 'Cameron']
for e in adlar:
    print(e)
    
for i, e in enumerate(adlar): #adlar listesini numaralandir diyorum aslinda.
                              #numaralar index olsun degeri-elemanim de e olsun.
    print(i, "indexindeki eleman:", e)
    
#defould olarak index 0 dan baslar. ama istersem degistiririm
for i, e in enumerate(adlar, start = 100):  #istersem 100den baslarim
    print(i, "lokasyonunda bulunan eleman:", e)
    
    
#zip()
#Farklı yapıların içinde paralel iterasyon yapmamızı sağlar. zip()

ogrenciler = ["ogrenci_1", "ogrenci_2", "ogrenci_3"]
notlar = [90,80,72]

for s, g in zip(ogrenciler, notlar): #iki listenin de ayni indexindeki elemanli zipler
    print(s, g) 
    
for e in zip(ogrenciler, notlar): #bu sekilde yazarsam tuple olarak yazar
    print(e) 
    
#zipsiz de yapabiliriz
for i in range(len(ogrenciler)): 
    print(ogrenciler[i], notlar[i])
    
    
#zip() ornegi

# Her ayki karı hesaplamak
satis = [3500.00, 76300.00, 67200.00]
maliyet = [56700.00, 21900.00, 12100.00]
for i in range(len(maliyet)):
    s = satis[i]
    c = maliyet[i]
    
    kar = s - c
    print(f'Total profit: {kar}')
    
    
#zip() ile
satis = [3500.00, 76300.00, 67200.00]
maliyet = [56700.00, 21900.00, 12100.00]
for s, c in zip(satis, maliyet):
    kar = s - c
    print(f'Total profit: {kar}')
    
    
#zip() ile Dictionary Yaratmak:
keys = ['isim', 'soyad', 'ulke', 'is']
values = ['Denis', 'Walker', 'Turkey', 'data scientist']

d = {}
for k, v in zip(keys, values): #key value pair i olusturur
    d[k] = v
print(d)
print(d["isim"])