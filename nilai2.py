import random
print(f'Program tebak angka by richie\n{"="*40}')
kom = random.randint(1,10)
user = int(input("Inilah game tebak angka\nMasukan angka dari 1-10 : "))

if kom == user :
    print("Anda benar")
elif user > 10 :
    print("masukkan angka dari 1 - 10 saja")
elif user >  kom :
    print(f"angka pilihan kom lebih kecil dari {user}")
else :
    print(f"angka pilihan kom lebih besar dari {user}")
