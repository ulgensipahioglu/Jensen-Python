#For-Function
#fonksiyonu listeye uygular

l = [1,2,3,4]

def apply(l, f):
    """ l bir liste, f listenin tüm elemanlarına uygulanacak fonksiyon 
    sonunda listenin orijinali elemanlarına fonksiyonun uygulanmış haliyle güncellenir """
    
    n = len(l) 
    
    for i in range(n):
        l[i] = f(l[i])

def kare(x):
    return x**2

apply(l, kare) # l listesinin her elemaninini kare fonksiyonuna sok
print(l)

def kup(x):
    return x**3

apply(l, kup)
print(l)


#Fonksiyonlar Listesini Belirli Bir Değere Uygulamak

def apply_funcs(f_list, x): 
    l = []
    for f in f_list:
        l.append(f(x))
        
    return l

print(apply_funcs([kare, kup], 5))