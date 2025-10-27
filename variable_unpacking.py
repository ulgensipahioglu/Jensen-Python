#birden fazla degeri birden fazla degiskene asign edebiliriz

x, y = (4, 7)
print(x)
print(y)

x, _ = (4, 7)
#y yi kullanmiceksam underscore kullanabilirim

#sayi esit olmazsa hata alirim
#x, y, z = (4, 7, 11, 4, 21)

x, y, *z = (4, 7, 11, 4, 21)

#basina yildiz koyarsam bastakiler sirayla gider kalani son degere kalanlari liste type inda verir
print(x,y,z)
print(type(x)) #int
print(type(y)) #int
print(type(z)) #list

#yildizi ortada kullanirsam bastakileri bastan sirayla sondakileri sondan sirayla atar.
#ortada kalanlari liste halinde yilidzliya atar.
#ONEMLI! fazladan 1 tane bile kalsa onu LISTE type inda atar
x, y, *z, t, u = (4, 7, 11, 4, 21, 32, 2)
print(x,y,z,t,u)
print(type(x)) #int
print(type(y)) #int
print(type(z)) #list
print(type(t)) #int
print(type(u)) #int

#bir coklu atamamda 1 yildizli kullanabilirim. yoksa hata alirirm



