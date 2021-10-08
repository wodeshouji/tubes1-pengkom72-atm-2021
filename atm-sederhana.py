'''
Tugas Besar 1
Pengenalan Komputasi
KU1102-72

Dosen: Rizal Dwi Prayogo, S.Si., M.Si., M.Sc.

Anggota Kelompok:
1. Matthew Mahendra / 16521497
2. Henry Anand Septian Radityo / 16521...
3. Richard Haris / 16521...
4. Kenny Benaya Nathan / 16521...

Deskripsi:  Program ATM-Sederhana dengan penyederhanaan yaitu hanya menggunakan 4 fungsi ATM yaitu transfer, tarik uang, cek saldo, 
            dan deposito

Kamus:
Dilengkapi seiring berjalan
'''

#Keterangan kartu sudah di pre-define lewat array di bawah ini
#Format array: Nama, Nomor Rekening, PIN, Saldo Rekening
kartu = ["Rick Sanchez", 61869, 123456, 1000000]

#Menu Tampilan Awal
print(". : WELCOME : .")
print(" BANK MACAN ASIA ")
pin = int(input("PLEASE ENTER YOUR IDENTIFICATION NUMBER: "))

#Conditional untuk pin
#Maksimum masukin pin 3 kali dengan 2 kali coba ulang. Lebih dari itu rekening diblokir
ulang = 0 #berapa kali salah

while (ulang < 2):
    if(pin == kartu[2]):
        print("Berhasil masuk")
        status_masuk = 'berhasil'
        ulang = 3
    elif(pin != kartu[2]):
        print("Incorrect PIN, please try again")
        status_masuk = 'gagal'
        ulang += 1
        pin = int(input("PLEASE ENTER YOUR IDENTIFICATION NUMBER: "))

#Cuci dosa terakhir
if(ulang == 2):
    if(pin == kartu[2]):
        status_masuk = 'berhasil'
    else:
        status_masuk = status_masuk

            
if(status_masuk == 'gagal'):
    print("Too many failed attempts. Your account has been suspended")
elif(status_masuk == 'berhasil'):
    print("\n=================")
    print("    MENU ATM    ")
    
    #MENU ATM STARTS HERE
    
    #Function cek saldo starts here
    def cek_saldo():
        saldo = kartu[3]
        print("Saldo Rekening Anda\n")
        print("====================\n")
        print("Rp", saldo)
    #Function cek saldo ends here
