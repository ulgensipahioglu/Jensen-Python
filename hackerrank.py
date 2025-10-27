from collections import defaultdict #eklemek sitedigim key sozlukte yoksa hata verme yeni key olustur demek icin defaultdict'i import ettim
d = defaultdict(list) # d adında yeni bir defaultdict nesnesi oluşturur. (list) yazmasi onemli. sebebi, sozlukte olmayan
                        #bir key e erismek istersem eger, o key icin yeni bir liste olustur sozluk icinde demis oluyorum.
d['python'].append("awesome") # ddict in icinde ptyhon adinda bi key yok. o yuzden once onu olusturuyo sonra o key e awesome valuesunu ekliyo
d['something-else'].append("not relevant") #ayni sekilde 'something-else' key i ve not relevant valusu
d['python'].append("language") #artik python key var bir liste olarak. o listeye yeni bi elemen ekliyo

for i in d.items(): #d sözlüğünün .items() metodunu kullanarak tüm (anahtar, değer) çiftleri üzerinde dönen bir döngü başlatır.
                    #i değişkeni, her döngüde bu çiftleri bir demet (tuple) olarak alır.
    print (i)
    
#output :   ('python', ['awesome', 'language'])
#           ('something-else', ['not relevant'])


from collections import defaultdict

# --- Girdileri Manuel Olarak Ayarlama ---
# input() ile almak yerine, A ve B gruplarını liste olarak biz tanımlıyoruz.

# A Grubu (n=5)
group_a = ['a', 'a', 'b', 'a', 'b']

# B Grubu (m=2) - Aranacak kelimeler
group_b = ['a', 'b']

# (İstersen 'c' gibi olmayan bir kelimeyi de test için ekleyebilirsin)
# group_b = ['a', 'b', 'c'] 

# --- Kodun Ana Mantığı ---

# 1. defaultdict'i oluştur
d = defaultdict(list)

print(f"Başlangıç (Boş Sözlük): {d}")

# 2. A Grubunu sözlüğe işle
# 'enumerate(group_a, 1)' kullanarak listeyi (index, kelime) olarak geziyoruz.
# '1' sayesinde indeks 0 yerine 1'den başlar (HackerRank'in istediği gibi).
print("\nA Grubu işleniyor...")
for i, kelime_a in enumerate(group_a, 1):
    d[kelime_a].append(i)
    print(f"  '{kelime_a}' eklendi -> Sözlük: {dict(d)}") # dict()'e çevirerek daha güzel yazdırıyoruz

print(f"\nİşlem Tamamlandı. Oluşan Sözlük:\n{dict(d)}")
print("-" * 30)
print("B Grubu Sorgulanıyor ve Çıktı Üretiliyor:")
print("-" * 30)

# 3. B Grubunu işle ve çıktı üret
for kelime_b in group_b:
    # 'kelime_b' ('a', sonra 'b') sözlükte (d) var mı?
    if kelime_b in d:
        # Varsa: O kelimenin pozisyon listesini al
        pozisyonlar = d[kelime_b]  # Örn: d['a'] -> [1, 2, 4]
        # Listeyi boşluklu string'e çevir ve yazdır
        print(" ".join(map(str, pozisyonlar)))
    else:
        # Yoksa: -1 yazdır
        print("-1")
        
        
#Bu kodu çalıştırdığınızda, sizden hiçbir girdi istemeyecek ve doğrudan aşağıdaki çıktıyı üretecektir:

#Başlangıç (Boş Sözlük): defaultdict(<class 'list'>, {})

# A Grubu işleniyor...
'''
  'a' eklendi -> Sözlük: {'a': [1]}
  'a' eklendi -> Sözlük: {'a': [1, 2]}
  'b' eklendi -> Sözlük: {'a': [1, 2], 'b': [3]}
  'a' eklendi -> Sözlük: {'a': [1, 2, 4], 'b': [3]}
  'b' eklendi -> Sözlük: {'a': [1, 2, 4], 'b': [3, 5]}
  '''

#İşlem Tamamlandı. Oluşan Sözlük:
#{'a': [1, 2, 4], 'b': [3, 5]}

#B Grubu Sorgulanıyor ve Çıktı Üretiliyor:
'''
1 2 4
3 5
'''

from collections import defaultdict
A = ['a', 'a', 'b', 'a', 'b']
B= ['a', 'b']
d = defaultdict(list)
for i, word in enumerate(A, 1):
    d[word].append(i)
    print(f"'{word}' added -> {dict(d)}")

for word in B:
    if word in d:
        positions = d[word]
        print(" ".join(map(str, positions)))
    else:
        print("-1")
        
