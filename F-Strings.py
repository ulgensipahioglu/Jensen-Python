#F-Strings

#f-string de yaptığımız tek şey aslında değişkenlerin değerlerini veya hesaplamaların sonucunu stringin içine gömmek.
#normalde bi sey yazdirirken typelari belirtmek lazim ama basina f koyarsan hepsini stringe kendi ceviriyo

x = 2
print("x in değeri" + " " + str(x))

#tek sefrde soyle yazariz
print(f"x in değeri {x}")

#icine gomecegimiz stringi tanimlarken -> f"...."
# gommek istegimiz degeri {} icinde. (birden cok ve farkli typelarda olabilir)
# f".....{}....{}.."

#suslu paratez icinde islem de yapabiliriz, fonksiyon, methot da tanimlayabilriz

print(f"x in değerinin iki fazlası {x+2}")

isim = input("İsim:")
print(f"verilen isim {isim}")

l = [1,2,3,4]
print(f"verilen liste {l}")

print(f"verilen isim {isim.capitalize()}") #capitalize python nin kendi fonksiyonudur. 
#basharfi buyutup yazar

#fonksiyon da yazabiliriz demistik

def kare(x):
    return x**2
x = 10
print(f"{x} sayisinin karesi {kare(x)}")
