#1
def hello(name):
    return f"Hello, {name}!"

hello = hello("Anna")
print(hello)

#2
def kdv(price, kdv = 0.25):
    kdvsiz_fiyat = price
    kdvli_fiyat = (price * kdv) + price
    return f"kdvsiz fiyat: {kdvsiz_fiyat}\nkdvli fiyat: {kdvli_fiyat}"

hesap1 = kdv(120)
print(hesap1)

hesap2 = kdv(120, 0.12)
print(hesap2)

#3
def fiyat(name, price, currency = "kr"):
    return f"{name} - {price} {currency}"
urun1 = fiyat("Pen",10)
print(urun1)
urun2 = fiyat(price = 50, name = "Book", currency="$")
print(urun2)

#4
def topla(*sayilar):
    total = sum(sayilar)
    return total
sonuc = topla(1,2,3,4)
print(sonuc)
sonuc2 = topla()
print(sonuc2)

#5
def tanim(**info):
    parca = []
    for key, value in info.items():
        parca.append(f"{key} = {value}")
    return " - ".join(parca) #direkt parca yazarsam listeyi verir

tanim1 = tanim(selam = "canim", nasilsin = "iyi msisin", aynen = "kanka")
print(tanim1)

#6
def list_name(title, *name, **meta):
    
    print(f"{title} List")
    print("davetli: ")

    for name in name:
        print(f"-{name}")
        
    print("Bilgiler:")
    bilgiler = []
    for key, value in meta.items():
        bilgiler.append(f"{key} = {value}")
        
    print (" - ".join(bilgiler))
    
list_name("Gäster", "Anna", "Erik", "Lisa", room="Aula", time="10:00")


#7
temps = [12, 5, 18, 9, 21, 3, 15]

cold = list(filter(lambda t: t<10, temps))

print(cold)

#8
numbers = [1, 2, 3, 4, 5]
duble_func = lambda t: t+2
double_obj = map(duble_func, numbers)
duble = list(double_obj)
print(duble)

#9
a = [1, 3, 5]
b = [10, 20, 30]

sum_func = lambda k,l: k+l
sum_obj = map(sum_func,a,b)
sum = list(sum_obj)
print(sum)


