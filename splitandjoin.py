#split()
#belli bir bolme kriterine gore (stringin icinde elemanlari bolen) stringi bolerek listeye ceviririz

s = "merhaba nasılsın ?"

#split()'in içine neye göre böleceğimizi yazarız.

#formul: string_adi.split("bolmek istedigin kriter")

print(s.split(" "))
#['merhaba', 'nasılsın', '?']


#hiç bir şey yazmazsak default olarak boşluğa göre böler.
print(s.split())  #['merhaba', 'nasılsın', '?']

s2 = "limon,portakal,elma"
print(s2.split())  #listede bosuk olmadigindan bosluga gire bolemez
#['limon,portakal,elma'] bu sonuc doner

print(s2.split(",")) #"," ile ayirir
#['limon', 'portakal', 'elma']



#join()
#listenin elemanları arasına belirtilen yapıyı koyup string'e dönüştürür.

# formul: "patern(elemanlar arasina konacak sey)".join(liste_adi)

l = ['limon', 'portakal', 'elma']

print(",".join(l)) #listeyi virgul ile ayirip string yapar
#limon,portakal,elma

s3 = "-".join(l) #bu sekilde degiskene atama da yapabilirim

print(s3)


