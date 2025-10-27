#Tuble ler immutabledir yani elemanlari degistirilemez.
#eleman degistime haric tum komutlar listle aynidir

#tuble_adi = (eleman1, eleman2, eleman3, ...) normal parantez ile yapilir
#ama parantez olmasa bile python arasi virgullu gorunce tapil sayar

demi = 23, 56, 78
print(type(demi)) #class tuble

konum = (10, 40)
print(konum[0]) #ilk eleman
print(konum[:]) #tum tabil 
print(konum[-1]) # son eleman
#konum[0] = 100 #hata alirim cunku eleman degismez

#farkli veri tipleri icerebilir

tapil = (1, "elma", 2.5, ["a","d"],(1,2,3))
print(tapil)
print(tapil[3]) #3. indexi verir ["a","d"]
#tapil[0] = 99 tuble lar degistirilmiyo hata verir
print(tapil[3][0]) #3. indexin ilk indexini verir a
tapil[3][0] = 55 #listin ilk elemanini degistirdim
print(tapil)


#eger iki degiskenin degerlerini degistirmek istersem normalde soyle yaparik

x = 1
y = 2
print(x, y)

temp = x
x = y
y = temp

print(x, y)

#ama bunu tabillarda tek satirda yapariz

i = 5
j = 6
print(i, j)

(i, j) = (j, i)
print(i, j)

#Belirli bir eleman listede veya tuple'da var mı diye in keyword'ü ile sorgu yapabilirim.
l = (1,2,3,4)
print(1 in l) #true doner
print(40 in l) #false doner