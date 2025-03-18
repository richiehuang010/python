print("="*10)
print("Program pertama saya")
print("="*10)
hasil = 0
user = int(input(f"Pilih Operasi\n1.kali\n2.bagi\n3.tambah\n4.kurang\nPilih no : "))
if user > 3 :
    print(f"tidak ada angka {user} di pilihan")
else :
    x = int(input("angka pertama : "))
    y = int(input("angka kedua : "))
    if user == 1 :
        hasil = x * y
    elif user == 2 :
        hasil = x / y
    elif user == 3 :
        hasil = x + y
    else :
        hasil = x - y

    print(f"Hasil = {hasil}")