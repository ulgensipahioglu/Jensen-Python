#Dictionaries
#suslu parantezle yapiliyor. icinde birden fazla degisken tutuyorsun
#dictionati_name = {key1:value1, key2:value2,...}  key value pair

notlar = {"Ali": 50, "Veli": 60, "Ayse": 567}
print(notlar["Ali"])  #index yazmiyurz da key yazip valueyu cagiriyoruz


#dictionari ler icinde dictionari icerebilir
ogrenciler = {"Deniz": {"not": 80, "no" : 789}, "Ege": {"not" : 100, "no" : 345}, "Ela":{"not" : 55, "no" : 678}}
print(ogrenciler)

print(ogrenciler["Ege"]) #sadece egenin notlari ve nsu gelir
print(ogrenciler["Ege"]["no"]) #sadece egenin no su gelir

#olamayn key i cagirirsam hata aliri
#print(ogrenciler["Mert"])

#index nosundan da cagiramam onu da key olarak algilar
#print(ogrenciler[1])

#valuelari degistirebilirim, eleme yapabilirim
print(ogrenciler["Deniz"]["not"])
ogrenciler["Deniz"] ["not"] = ogrenciler["Deniz"] ["not"]+ 5
print(ogrenciler["Deniz"]["not"])


#len() kac key var onu verir
print(len(ogrenciler))

#eleman eklemek
ogrenciler["Mert"] = 58
print(ogrenciler)

#eleman silmek del
del ogrenciler["Mert"]
print(ogrenciler)

#bos bir dictionari yaratmak
d = {}
d[1] = "a" #1 key ine a value sunu atadim
print(d)

#in, icinde boyle bi key var mi diye bakar
print("Deniz" in ogrenciler) #key arar TRUE
print("80" in ogrenciler) #value ya bakmak FALSE
print(80 in ogrenciler) #FALSE

