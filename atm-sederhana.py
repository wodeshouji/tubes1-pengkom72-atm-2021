'''
Tugas Besar 1
Pengenalan Komputasi
KU1102-72

Dosen: Rizal Dwi Prayogo, S.Si., M.Si., M.Sc.

Anggota Kelompok:
1. Matthew Mahendra / 16521497
2. Henry Anand Septian Radityo / 16521507
3. Richard Haris / 16521...
4. Kenny Benaya Nathan / 16521527

Deskripsi:  Program ATM-Sederhana dengan penyederhanaan yaitu hanya menggunakan 4 fungsi ATM yaitu transfer, tarik uang, cek saldo, 
            dan deposito

Kamus:
'''

#Keterangan kartu sudah di pre-define lewat array di bawah ini
#Format array: Nama, Nomor Rekening, PIN, Saldo Rekening
kartu = ["Rick Sanchez", 61869, 123456, 1000000]

#Saldo di ATM
#Untuk tarik uang
saldo_atm = 1000000

#Menu Tampilan Awal
print("========================")
print(" BANK MACAN ASIA ")
print(". : WELCOME : .")
print("========================")
pin = int(input("PLEASE ENTER YOUR PERSONAL IDENTIFICATION NUMBER: "))

#Conditional untuk pin
#Maksimum masukin pin 3 kali dengan 2 kali coba ulang. Lebih dari itu rekening diblokir
ulang = 0 #berapa kali salah

while (ulang < 2):
    if(pin == kartu[2]):
        #print("Berhasil masuk") #just for testing
        status_masuk = 'berhasil'
        ulang = 3
    elif(pin != kartu[2]):
        print("Incorrect PIN, please try again")
        status_masuk = 'gagal'
        ulang += 1
        pin = int(input("PLEASE ENTER YOUR PERSONAL IDENTIFICATION NUMBER: "))

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
    print("=================\n")
        #Fuction list:
    #Function transfer rekening starts here
    
    #Fuction transfer rekening ends here

    #Function deposito starts here

    #Function deposito ends here

    #Function cek saldo starts here

    #Function cek saldo starts here
    def cek_saldo():
        saldo = kartu[3]
        print("Saldo Rekening Anda")
        print("Rp", saldo) #Ambil keterangan saldo
        print("====================")
    #Function cek saldo ends here
    
    #MENU ATM STARTS HERE
    menu = 0
    while menu<1:
        print("====================")
        print("1. Cek Saldo")
        print("2. Transfer")
        print("3. Trading Simulation/Deposito")
        print("4. Transaksi Selesai")
        print("====================")
        a = int(input("Pilih menu: "))
        if (a==1):
            cek_saldo()
        elif (a==2):
            transfer()
        elif (a==3):
            deposito()
        elif (a==4):
            menu +=1
        else:
            print("Masukkan menu yang sesuai (1-4)")
    print("Transaksi selesai, Terima kasih!")