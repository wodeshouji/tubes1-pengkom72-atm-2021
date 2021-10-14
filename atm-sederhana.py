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
#Format array: Nama, Nomor Rekening, PIN, Saldo Rekening, Punya Deposito atau Tidak
kartu = ["Rick Sanchez", 61869, 123456, 1000000, 0]

#Saldo di ATM
#Untuk tarik uang
saldo_atm = 5000000

#Menu Tampilan Awal
print("========================")
print(" BANK MACAN ASIA ")
print(". : WELCOME : .")
print("========================")
#pin = int(input("PLEASE ENTER YOUR PERSONAL IDENTIFICATION NUMBER: "))

#Conditional untuk pin
#Maksimum masukin pin 3 kali dengan 2 kali coba ulang. Lebih dari itu rekening diblokir
ulang = 0 #sudah mengulang beberapa kali

while (ulang < 3):
    pin = int(input("PLEASE ENTER YOUR PERSONAL IDENTIFICATION NUMBER: "))
    if(pin == kartu[2]):
        #print("Berhasil masuk") #just for testing
        status_masuk = 'berhasil'
        ulang = 3
    elif(pin != kartu[2]):
        print("Incorrect PIN, please try again")
        status_masuk = 'gagal'
        ulang += 1
        #pin = int(input("PLEASE ENTER YOUR PERSONAL IDENTIFICATION NUMBER: "))
            
if(status_masuk == 'gagal'):
    print("Too many failed attempts. Your account has been suspended")
elif(status_masuk == 'berhasil'):
    #Function list:
    
    #Exit sequence function: untuk exit atm setelah sebuah transaksi selesai tanpa harus kembali ke menu atm
    def exit_sequence():
        global menu
        exit_confirm = 0
        while exit_confirm < 1:
            exit = input("Apakah Anda ingin membuat transaksi lain? (y/n) ")
            if(exit == 'y'):
                exit_confirm += 1
            elif(exit == 'n'):
                exit_confirm += 1
                menu += 1
            else:
                print("Masukkan y/n")

    #Function transfer rekening starts here
    def transfer():
        global saldo_atm
        rek_transfer = int(input('Masukkan nomor rekening yang dituju: '))
        nominal = int(input('Masukkan jumlah nominal uang yang akan ditransfer: '))
        # layar konfirmasi
        print('====================')
        print('Konfirmasi Transaksi')
        print('====================')
        print('TRANSFER')
        print('Nomor rekening   : ' + str(rek_transfer))
        print('Jumlah           : Rp' + str(nominal))
        print('Saldo anda akan berkurang dan berpindah ke rekening penerima')
        konfirmasi = 0     # buat ngulang konfirmasi transfer klau ga valid
        while konfirmasi < 1:
            confirm = input('Transaksi dilanjutkan? (y/n): ')
            if confirm == 'y':
                print('====================')
                # Kalau saldo di ATM atau saldo di rekening tidak cukup
                if(nominal > kartu[3] or nominal > saldo_atm): 
                    print("Saldo tidak cukup")
                else:
                    kartu[3] -= nominal     # kurangi jumlah saldo di rekening dengan jumlah uang yang ditransfer
                    saldo_atm -= nominal    # kurangi jumlah saldo di atm dengan jumlah uang yang ditransfer
                    print("Transaksi Anda sudah berhasil")
                    print('Sisa saldo anda: Rp' + str(kartu[3]))
                konfirmasi += 1 # biar selesai
            elif confirm == 'n':
                konfirmasi += 1
            else:
                # biar ngulang jawabannya yang bener
                print('Masukkan menu yang sesuai')
        
        #exit atm
        exit_sequence()
    #Fuction transfer rekening ends here

    #Function deposito starts here
    def deposito():
        if(kartu[4] == 0):
            Punya_deposito = False
        else:
            Punya_deposito = True
        
        print("1.Pembukaan Rekening Deposito")
        print("2.Informasi Deposito")
        print("3.Pencairan Deposito")
        print("4.Kembali")
        Menu = int(input("Pilih menu: "))
        if(Menu == 1):
            if(Punya_deposito == False):
                print("Selamat Datang di Menu Pembukaan Rekening Deposito")
                print("--------------------------------------------------")
                print("")
                print("Peraturan Deposito")
                print("--------------------------------------------------")
                print("1.Suku bunga sebesar 2% per bulan")
                print("2.Nominal minimum deposito sebesar Rp1000000")
                print("3.Jangka waktu deposito yaitu 1 bulan, 3 bulan, 6 bulan, 9 bulan, dan 12 bulan")
                print("4.Biaya pajak penghasilan sebesar 30% dari nominal bunga")
                print("5.Pencairan dana deposito tidak dapat dilakukan pada saat yang bersamaan dengan periode pembukaan rekening deposito")
                print("")
                
                Nomor_Rekening = int(input("Silakan masukkan nomor rekening Anda: "))
                while(Nomor_Rekening != kartu[1]):
                    print("Nomor rekening yang Anda masukkan salah.")
                    Nomor_Rekening = int(input("Silakan masukkan nomor rekening Anda: "))
                
                Nominal_Deposito = int(input("Nominal Deposito (IDR):Rp"))
                while(Nominal_Deposito < 1000000):
                    print("Nominal deposito tidak memenuhi nominal minimum deposito.")
                    Nominal_Deposito = int(input("Nominal Deposito (IDR):Rp"))
                while(Nominal_Deposito < kartu[3]):
                    print("Saldo rekening tidak mencukupi.")
                    Nominal_Deposito = int(input("Nominal Deposito (IDR):Rp"))
                
                global Jangka_Waktu
                Jangka_Waktu = int(input("Jangka Waktu (bulan): "))
                while(Jangka_Waktu != 1 and Jangka_Waktu != 3 and Jangka_Waktu != 6 and Jangka_Waktu != 9 and Jangka_Waktu != 12):
                    print("Tidak ada pilihan jangka waktu tersebut.")
                    Jangka_Waktu = int(input("Jangka Waktu (bulan): "))

                PIN = int(input("Masukkan PIN Anda: "))
                while(PIN != kartu[2]):
                    print("PIN yang dimasukkan salah.")
                    PIN = int(input("Masukkan PIN Anda: "))

                kartu[3] = kartu[3] - Nominal_Deposito
                kartu[4] = Nominal_Deposito
                
                print("Pembukaan Rekening Deposito Berhasil!")
                print("Informasi tentang deposito dapat dilihat pada menu Informasi Deposito.")
                deposito()
            else:
                print("Anda sudah memiliki rekening deposito.")
                deposito()

        if(Menu == 2):
            if(Punya_deposito == True):
                Nominal_Deposito = kartu[4]
                Nomor_Rekening = kartu[1]
                print("Informasi Deposito")
                print("------------------")
                print("")
                print("Total Dana Deposito")
                print("Rp"+str(Nominal_Deposito))
                print("------------------")
                print("")
                print("Nomor Rekening Dana Deposito: "+str(Nomor_Rekening))
                print("Nama: "+kartu[0])
                print("Suku bunga: 2% per bulan")
                print("Jangka waktu: "+str(Jangka_Waktu)+" bulan")
                Bunga = (1.02**Jangka_Waktu)*Nominal_Deposito - Nominal_Deposito
                Pajak = 0.3*Bunga
                Estimasi = int(Nominal_Deposito + Bunga - Pajak) 
                print("Estimasi Hasil Deposito: Rp"+str(Estimasi))
                deposito()
            else:
                print("Silakan membuka rekening deposito terlebih dahulu.")
                deposito()

        if(Menu == 3):
            if(Punya_deposito == True):
                print("Anda tidak dapat mencairkan deposito pada saat yang sama dengan periode pembukaan rekening deposito Anda.")
                deposito()
            else:
                print("Silakan membuka rekening deposito terlebih dahulu.")
                deposito()

        if(Menu == 4):
            print("", end='')
    #Function deposito ends here

    #Function cek saldo starts here
    def cek_saldo():
        saldo = kartu[3] #ambil saldo yang ada di kartu
        print("Saldo Rekening Anda")
        print("Rp", saldo) #Ambil keterangan saldo
        print("====================")

        #exit transaksi
        exit_sequence()
    #Function cek saldo ends here
    
    #Function tarik uang starts here
    def tarik_uang():
        global saldo_atm #saldo_atm adalah variabel global
        konfirmasi = 0
        jmlh_uang = int(input("Masukkan jumlah uang yang akan Anda tarik: "))
        print('====================')
        print('Konfirmasi Transaksi') #konfirmasi akan menarik tunai sebesar jmlh_uang
        print('====================')
        print('    TARIK TUNAI     ')
        print('Nomor Rekening: {}'.format(kartu[1]))
        print("Saldo Anda akan berkurang sebesar Rp{} untuk ditarik secara tunai".format(jmlh_uang))

        while konfirmasi < 1:
            confirm = input("Transaksi dilanjutkan?(y/n) ") #input konfirmasi apakah transaksi akan dilanjutkan atau tidak
            if(jmlh_uang > kartu[3] or jmlh_uang > saldo_atm): #Kalau saldo di ATM atau saldo di rekening tidak cukup print saldo tidak cukup (error)
                print("Saldo tidak cukup")
                konfirmasi += 1 #terminasi
            else:
                if(confirm == 'y'):
                    kartu[3] -= jmlh_uang #kurangi jumlah saldo di rekening dengan jumlah uang yang ditarik
                    saldo_atm -= jmlh_uang #kurangi jumlah saldo di atm dengan jumlah uang yang ditarik
                    print("Transaksi berhasil")
                    print("Sisa saldo Anda Rp{}".format(kartu[3])) #berikan sisa saldo di rekening
                    konfirmasi += 1 #terminasi

                elif(confirm == 'n'):
                    print("Transaksi dibatalkan")
                    konfirmasi += 1 #terminasi

                else:
                    print("Masukkan y/n ")
            
        #exit transaksi tarik tunai
        exit_sequence()
    #Function tarik uang ends here

    #MENU ATM STARTS HERE
    menu = 0
    while menu<1:
        print("\n====================")
        print("    MENU ATM    ")
        print("====================")
        print("1. Cek Saldo")
        print("2. Transfer")
        print("3. Trading Simulation/Deposito")
        print("4. Tarik Uang")
        print("5. Transaksi Selesai")
        print("====================")
        a = int(input("Pilih menu: "))
        if (a==1):
            cek_saldo()
        elif (a==2):
            transfer()
        elif (a==3):
            deposito()
        elif (a==4):
            tarik_uang()
        elif (a==5):
            menu += 1
        else:
            print("Masukkan menu yang sesuai (1-4)")
    print("Transaksi selesai, Terima kasih!")
