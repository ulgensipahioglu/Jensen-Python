for c in "hey": #hey in elemanlarini gez ve yazdir
    print(c)


s = "hey"
for d in s:
    print(d)


v = len(s)           #for while ile de yazilabilir. ama while for ile yazilamaz
index = 0

while index < v:
    print(s[index])
    index += 1

x = 1
for x in range(5):
    print(x)
    
    
toplam = 0
for i in range(5):
    toplam += i
print(toplam)



ustu = 1
for i in range(5):
    ustu *=5
print(ustu)


ustu = 1
for _ in range(5): #kullanmadigim degisken icin _ kullanabilirim
    ustu *=5
print(ustu)

# continue and break

for i in range(10):
    if i == 3:
        break
    print(i)
    
    
x = 0
while x <10:
    x += 1
    if x== 3:
        break
    print(x)
    
    
x = 0
while x <10:
    print(x)  #printi buraya yazarsam arttirmadan yazar 012
    x += 1
    if x== 3:
        break
    
    
for i in range(10):
    if i == 3:
        print("hey") #usttekini yapa
        continue # kendisinden 1 sonraki satiri atlar digerinden devam eder
    print(i) #alttakini yapmaz kosulu sagladiginda
print("merhaba") #bir sonraki satira gecer



x = 0

while x < 10:
    x += 1
    
    if x == 3:
        continue #3 u atlar devam eder
    
    print(x)
    
    
i=0
while(i<10):
    if(i==3 or i==5):
      continue
    print("i: ",i)
    i=i+1
    
    
    
    
