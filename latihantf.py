login = ""
saldo = 50000
x = 123
pin = int(input("Masukkan pin anda: "))
if pin == x :
    print("login berhasil")
    login = "berhasil"
else : print("login gagal")

if login == "berhasil" :
    user = int(input("Silahkan pilih transaksi\n1,Liat Saldo\n2.Tarik Saldo\n3. Setor tunai\nMasukkan angka :"))

if user == 1 :
    print(f"Saldo anda {saldo}")
elif user == 2 :
    tarik_tunai = int(input("Masukkan jumlah uang yang ingin anda tarik: "))
    if tarik_tunai < saldo :
        saldo -= tarik_tunai
        print(f"Sisa saldo anda adalah {saldo}")
    else : print("Saldo anda tidak cukup")

elif user == 3 :
    setor_tunai = int(input("Masukkan jumlah uang yang akan disetor: "))
    user = int(input("Masukkan pin anda untuk proses KOMFIRMASI: "))
    if user == x :
        saldo += setor_tunai
        print(f"Isi saldo anda sekarang adalah {saldo}")
    else : print("Proses KONFIMASI gagal karena pin yg anda masukkan salah")
else : print("Angka yg anda masukkan tidak ada di pilihan")
