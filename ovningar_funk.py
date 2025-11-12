# Övningar – Funktioner, lambda, map, filter, zip m.m. (Instruktioner)
#1) Hälsningsfunktion – enkel retur
def hello(name):
    return f"Hello, {name}!"

hello = hello("Anna")

print(hello)

#2) Pris med moms – default-argument
def  vat(price, vat=0.25):
    vat_included = (price * vat) + price
    vat_excluding = price
    return f"Price excluding VAT:{vat_excluding}\n"f"Price including VAT:{vat_included}"

result_default = vat(120)
print("--- Default VAT (0.25) ---")
print(result_default)

alternative_vat = 0.12
alternative_result = vat(120, alternative_vat)

print("\n--- Alternative VAT (0.12) ---")
print(alternative_result)
    
#3) Formaterad etikett – keyword-argument
def label(name,price,currency = "kr"):
    return f"{name} - {price} {currency}"

label1 = label("Penna", 10)
print(label1)

label2 = label(price=10, name="Penna")
print(label2)

label3 = label("Bok", 99, currency="$")
print(label3)

#4) Summera många tal – *args

def summera(*tal): #kac tane deger gelicek bilmedigimiz zamanlar *args kullaniriz
    total = sum(tal)
    
    return total

result_with_args = summera(2,5,3,10)
print(result_with_args)

result_without_args = summera()
print(result_without_args)

#5) Slå ihop nyckelvärden – **kwargs #anahtar deger ciftini birlestirme (Keyword Arguments)
def description(**info):
    parts = [] #bos liste olustur
    for key,value in info.items():
        parts.append(f"{key}={value}") # Bellekte sadece listeye eklenir, kopyalama yapılmaz.
    return ", ".join(parts) #tek sefrde nihai dizi olusturulur.

call1 = description(titel = "Adventure", year=2025, director="A. Nova")
print(f"Result: {call1}")

call2 = description(film = "Incepstion", director = "Nolan", puan = 8.8)
print(f"Result: {call2}")

#6) Många namn + metadata – kombinera *args/**kwargs
def list_names(title, *name, **meta):
    
    print(f"{title} List")
    print("Attendees:")
    
    for name in name:
        print(f"-{name}")
            
    print("Metadata:") #(Key=Value Pairs)
    meta_parts = []
    for key, value in meta.items():
        meta_parts.append(f"{key} = {value}")
    
    print(", ".join(meta_parts))
    
list_names("Gäster", "Anna", "Erik", "Lisa", room="Aula", time="10:00")

#7) Temperaturfilter – filter + lambda
#1- klasik yontem 
temps = [12, 5, 18, 9, 21, 3, 15]
def temperatur_filter(list):
    cold_list = []
    for i in temps:
        if i < 10:
            cold_list.append(i)
    return cold_list
new_list = temperatur_filter(temps)
print(new_list)


#2-Pythonun kendi Lamda ve filter metoduyla:
temps = [12, 5, 18, 9, 21, 3, 15]

# Lambda fonksiyonu: Bir sayının 10'dan küçük olup olmadığını kontrol eder.
# 'temp' buradaki girdi değişkenimizdir (yani listedeki her bir sayı).
# lambda temp: temp < 10 = (TRUE)
filter_func = lambda temp: temp < 10

# filter() fonksiyonu: Listeyi alır ve sadece True döndüren elemanları tutar.
# filter() bir 'filter object' döndürdüğü için, bir listeye dönüştürmemiz gerekir.
cold = filter(filter_func, temps)

# Filter nesnesini (cold) listeye dönüştürerek sonucu elde et
cold = list(cold)

# Sonucu yazdır
print(cold)



#3- Tek adımda liste oluşturma:
temps = [12, 5, 18, 9, 21, 3, 15]

cold = list(filter(lambda t: t < 10, temps))

print(cold)
        

#8) Dubbla talen – map + lambda
numbers = [1, 2, 3, 4, 5]

#Lambda fonksiyonu: Listenin her elemanını (t) alır ve 2 ile çarpar.
double_func = lambda t: t*2

# map() fonksiyonu: iki_kat_alma_fonksiyonu'nu 'tal' listesindeki her elemana uygular.
# map() bir 'map object' döndürür.
double_obj = map(double_func,numbers)

double = list(double_obj)

print(double)


#9) Två listor → summerade par – map + lambda med två iterables
a = [1, 3, 5]
b = [10, 20, 30]

sum_func = lambda k, l: k + l
sum_obj = map(sum_func,a,b)
sum = list(sum_obj)
print(sum)

#10) Filtrera ord på längd – filter + lambda
ord = ["sol", "måne", "stjärna", "moln", "regn", "is"]
lengt_world = lambda ord: len(ord) >= 4
list1 = filter(lengt_world,ord)
list1 = list(list1)
print(list1)
    
        
        
    