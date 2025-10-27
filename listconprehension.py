#List Comprehensions LISTE URETICILERI

#[ yapilacak_islem for eleman in liste ]
# 
# Diyelim ki 1'den 10'a kadar olan sayıların karelerinden bir liste oluşturmak istiyorum. 
# Bunu aşağıdaki gibi yapabilirim.

squares = []

for i in range(1,11):
    squares.append(i*i)
print(squares)

#Bunun aynısını list comprehension kullanarak da yapabiliriz.

squares = [i * i for i in range(1,11)]  #ayni soucu tek satirda alirim
print(squares)


# list comprehension ve fonksiyon mantığını birleştirme

def cube(x): #cube adinda bir fonksiyon olusturalim
    return x * x * x # x ** 3 

cubes = [cube(x) for x in range(1,11)] 
# aslinda soyle demis oluyoruz: 1den 10a kadar, cube fonsiyonunu calistir
#cube fonksiyonunu kullanarak cube adinda bir liste olusturur
print(cubes)

#List Comprehension'larda Conditional Yapıların Kullanılması

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(squares)

#su sekide tek sayilari yazdirabiliriz: (uzun olur)
odd_squares = [] #bos bir tek karesayilar listesi olustur
  
for e in squares: #squares listesi elemanlarini tek tek e ye ata. 
    
    if e % 2 == 1:  # e tek oldugu surece odd_square listesine append et. 
        odd_squares.append(e)
print(odd_squares)
#[1, 9, 25, 49, 81]

# squares listindeki tek elemanlardan yeni bir liste yaratmak

odd_squares = [e for e in squares if e % 2 == 1] 
#bu sekilde kisaca da ayni listeyi elde ederim
print(odd_squares)
#[1, 9, 25, 49, 81]

# bu test mantığını fonksiyonla da sağlayabilirdik
def is_odd(x): 
    
    if x % 2 == 0:
        return False
    
    if x % 2 == 1:
        return True
    
odd_squares = [e for e in squares if is_odd(e)]
print(odd_squares)


def empty(x): 
    
    if x % 2 == 0:
        return False
    
    if x % 2 == 1:
        return False
empty_squares = [e for e in squares if empty(e)]
print(empty_squares)

def is_even(x):
    
    if x % 2 == 0:
        return True
    
    if x % 2 == 1:
        return False
even_squares = [e for e in squares if is_even(e)]
print(even_squares)


print(squares)
weird_squares = [e if e % 2 == 0 else -1 for e in squares]
print(weird_squares)
#[-1, 4, -1, 16, -1, 36, -1, 64, -1, 100]

ultra_weird_squares = [e if e % 2 == 0 else -1 for e in squares if is_even(e)]
print(ultra_weird_squares)
#[4, 16, 36, 64, 100]


#Set Comprehension

numbers = [1,2,3,4,5,6,7,1,2]
set_numbers = {s for s in numbers if s in [1,2,3,4,5,6,1,2]}
print(set_numbers) #sete cevirdi

#Dictionary Comprehension

square_dict = {e:e * e for e in range(1,11)} #key 1den11e kadar olan sayi olsun, value onun karesi olsun
print(square_dict)

print(square_dict[9]) #81


#Nested List Comprehension

#[ islem for dis_dongu_elemani in dis_liste for ic_dongu_elemani in ic_liste ]

m = [[j for j in range(7)] for i in range(5)]

m = [[j for j in range(7)] for _ in range(5)] #ayni sey i kullanilmiyo _ yazabiliriz

#range7 yani 0dan 7ye (7 haric) bir liste yazdir. o listenin elemanlari bu sefer j olsun ve bir daha range7 liste yazdir.

print(m) 
'''
[[0, 1, 2, 3, 4, 5, 6],
 [0, 1, 2, 3, 4, 5, 6],
 [0, 1, 2, 3, 4, 5, 6],
 [0, 1, 2, 3, 4, 5, 6],
 [0, 1, 2, 3, 4, 5, 6]]'''
 
 
m = [[10, 11, 12], [13, 14], [15, 16, 17, 18]] 

for l in m:
    print(l) # m nin elemanarini yazdir. 3 tane liste elemani var.
'''
[10, 11, 12]
[13, 14]
[15, 16, 17, 18]'''

new_m = [] #bos liste olustur
for l in m: #l m nin elemanlari
    print(l)  
    for e in l: #e l nin elemanlari
        new_m.append(e) #listeye append le
        print(e)

'''
[10, 11, 12]
10
11
12
[13, 14]
13
14
[15, 16, 17, 18]
15
16
17
18'''
  
print(new_m) #[10, 11, 12, 13, 14, 15, 16, 17, 18] tum elemanlari gezmis olduk

# matrixi list comprehension ile flat etmek (daha kisa)

flatten_m = [e for l in m for e in l] #e l nin elemeani, l m nin elemeni.
print(flatten_m)

# Sadece çift değerleri kabul edecek
flatten_m = [e for l in m for e in l if e % 2 == 0] #if ekliyoruz
print(flatten_m)

