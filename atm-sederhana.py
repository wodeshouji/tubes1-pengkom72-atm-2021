'''
Tugas Besar 1
Pengenalan Komputasi
KU1102-72

Dosen: Rizal Dwi Prayogo, S.Si., M.Si., M.Sc.

Anggota Kelompok:
1. Matthew Mahendra / 16521497
2. Henry Anand Septian Radityo / 16521507
3. Richard Haris / 16521501
4. Kenny Benaya Nathan / 16521527

Deskripsi:  Program ATM-Sederhana dengan penyederhanaan yaitu hanya menggunakan 4 fungsi ATM yaitu transfer, tarik uang, cek saldo, 
            dan deposito
'''

#Keterangan kartu sudah di pre-define lewat array di bawah ini
#Format array: Nama, Nomor Rekening, PIN, Saldo Rekening, Punya Deposito atau Tidak, Dana Deposito
kartu = ["Rick Sanchez", 61869, 123456, 1000000, False, 0]

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
        return

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
                if(nominal > kartu[3]): 
                    print("Saldo tidak cukup")
                else:
                    kartu[3] -= nominal     # kurangi jumlah saldo di rekening dengan jumlah uang yang ditransfer
                    print("Transaksi Anda sudah berhasil")
                    print('Sisa saldo anda: Rp' + str(kartu[3]))
                konfirmasi += 1 # biar selesai
            elif confirm == 'n':
                konfirmasi += 1
                # masuk ke layar menu
            else:
                # biar ngulang jawabannya yang bener
                print('Masukkan menu yang sesuai')
        
        #exit atm
        exit_sequence()

        return
    #Fuction transfer rekening ends here

    #Function deposito starts here
    def deposito():
        if(kartu[4] == False):  # Apakah pengguna memiliki rekening deposito?
            Punya_deposito = False  # Jika kartu[4] bernilai false, maka belum punya deposito
        else:
            Punya_deposito = True # Jika kartu[4] tidak bernilai false, maka sudah punya deposito
        
        # layar menu deposito
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
        print("1.Pembukaan Rekening Deposito")
        print("2.Informasi Deposito")
        print("3.Pencairan Deposito")
        print("4.Kembali")
        Menu = int(input("Pilih menu: "))
        if(Menu == 1): # Menu Pembukaan Rekening Deposito
            if(Punya_deposito == False):  # Jika belum punya deposito, maka harus buka rekening deposito dahulu
                if(kartu[3] < 1000000): # Jika saldo rekening anda tidak mencukupi ketentuan minimum deposito, maka anda tidak dapat membuka rekening deposito
                    print("Saldo rekening anda tidak cukup untuk membuka rekening deposito sesuai peraturan yang disebutkan.")
                    print("", end='') # kembali ke menu awal
                else:
                    Nomor_Rekening = int(input("Silakan masukkan nomor rekening Anda: ")) # Masukkan nomor rekening anda sebagai verifikasi bahwa pengguna adalah anda sendiri
                    while(Nomor_Rekening != kartu[1]):  # ika nomor rekening yang dimasukkan tidak sesuai dengan nomor rekening pengguna, maka masukkan ulang nomor rekening hingga sesuai
                        print("Nomor rekening yang Anda masukkan salah.")
                        Nomor_Rekening = int(input("Silakan masukkan nomor rekening Anda: "))
                    
                    Nominal_Deposito = int(input("Nominal Deposito (IDR):Rp")) # Masukkan nominal deposito yang diinginkan
                    while(Nominal_Deposito < 1000000 or Nominal_Deposito > kartu[3]):  # Jika nominal deposito kurang dari syarat minimum dari peraturan bank yang disebutkan sebelumnya atau saldo rekening tidak mencukupi nominal yang diinginkan, masukkan nominal deposito hingga sesuai dengan ketentuan yang disebutkan
                        print("Nominal deposito tidak memenuhi ketentuan nominal minimum deposito atau saldo rekening tidak mencukupi nominal yang diinginkan.")
                        Nominal_Deposito = int(input("Nominal Deposito (IDR):Rp"))
                    
                    global Jangka_Waktu # Membuat variabel global agar dapat digunakan di menu 2, yaitu Informasi Deposito
                    Jangka_Waktu = int(input("Jangka Waktu (bulan): "))  # Masukkan jangka waktu deposito yang diinginkan
                    while(Jangka_Waktu != 1 and Jangka_Waktu != 3 and Jangka_Waktu != 6 and Jangka_Waktu != 9 and Jangka_Waktu != 12):  # Jika jangka waktu tidak sesuai dengan peraturan deposito, masukkan ulang hingga sesuai peraturan
                        print("Tidak ada pilihan jangka waktu tersebut.")
                        Jangka_Waktu = int(input("Jangka Waktu (bulan): "))

                    PIN = int(input("Masukkan PIN Anda: ")) # Masukkan PIN rekening anda
                    while(PIN != kartu[2]):  # Jika PIN rekening anda tidak sesuai dengan yang sebenarnya, masukkan ulang PIN hingga sesuai
                        print("PIN yang dimasukkan salah.")
                        PIN = int(input("Masukkan PIN Anda: "))

                    kartu[3] = kartu[3] - Nominal_Deposito # Saldo rekening yang tersisa sama dengan saldo rekening awal dikurangi nominal deposito
                    kartu[5] = Nominal_Deposito # Saldo rekening deposito sama dengan nominal deposito
                    kartu[4] = True 
                    
                    print("Pembukaan Rekening Deposito Berhasil!")
                    print("Informasi tentang deposito dapat dilihat pada menu Informasi Deposito.")
                    deposito() # kembali ke layar menu deposito
            else: # Jika anda telah memiliki rekening deposito, maka tidak perlu membuka rekening deposito lagi
                print("Anda sudah memiliki rekening deposito.")
                deposito() # kembali ke layar menu deposito

        elif(Menu == 2): # Menu Informasi Deposito
            if(Punya_deposito == True): # Jika anda telah memiliki rekening deposito, informasi deposito anda dapat dilihat di bawah ini
                Nominal_Deposito = kartu[5]
                Nomor_Rekening = kartu[1]
                print("Informasi Deposito")
                print("------------------")
                print("")
                print("Total Dana Deposito")
                print("Rp"+str(Nominal_Deposito)) # Nominal deposito
                print("------------------")
                print("")
                print("Nomor Rekening Dana Deposito: "+str(Nomor_Rekening)) # Nomor rekening
                print("Nama: "+kartu[0]) # Nama pemilik rekening
                print("Suku bunga: 2% per bulan")
                print("Jangka waktu: "+str(Jangka_Waktu)+" bulan") # Jangka waktu deposito
                Bunga = (1.02**Jangka_Waktu)*Nominal_Deposito - Nominal_Deposito # Bunga deposito
                Pajak = 0.3*Bunga # Pajak deposito
                Estimasi = int(Nominal_Deposito + Bunga - Pajak) # Estimasi hasil deposito
                print("Estimasi Hasil Deposito: Rp"+str(Estimasi))
                deposito() # kembali ke layar menu deposito
            else: # Jika anda belum memiliki rekening deposito, maka buat rekening deposito terlebih dahulu
                print("Silakan membuka rekening deposito terlebih dahulu.")
                deposito() # kembali ke layar menu deposito

        elif(Menu == 3): # Menu pencairan dana deposito
            if(Punya_deposito == True): # Jika anda telah memiliki rekening deposito, pada saat yang bersamaan dengan periode pembukaan rekening deposito, anda tidak dapat mencairkan dana deposito anda sesuai peraturan yang ditetapkan
                print("Berdasarkan peraturan, Anda tidak dapat mencairkan deposito pada saat yang sama dengan periode pembukaan rekening deposito Anda.")
                deposito() # kembali ke layar menu deposito
            else: # Jika anda belum memiliki rekening deposito, maka buat rekening deposito terlebih dahulu
                print("Silakan membuka rekening deposito terlebih dahulu.")
                deposito() # kembali ke layar menu deposito

        elif(Menu == 4): # Menu untuk kembali ke menu ATM awal
            print("", end='') # kembali ke menu ATM awal
        
        else: # Jika memilih menu yang tidak tersedia, maka kembali ke layar menu deposito dan masukkan ulang nomor menu hingga sesuai dengan yang tersedia di layar menu deposito
            print("Harap masukkan nomor menu yang tersedia.")
            deposito() # kembali ke layar menu deposito
    
        return
    #Function deposito ends here

    #Function cek saldo starts here
    def cek_saldo():
        saldo = kartu[3] #ambil saldo yang ada di kartu
        print("Saldo Rekening Anda")
        print("Rp", saldo) #Ambil keterangan saldo
        print("====================")

        #exit transaksi
        exit_sequence()

        return
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
        return
    #Function tarik uang ends here

    #MENU ATM STARTS HERE
    menu = 0
    while menu<1:
        print("\n====================")
        print("    MENU ATM    ")
        print("====================")
        print("1. Cek Saldo")
        print("2. Transfer")
        print("3. Deposito")
        print("4. Tarik Tunai")
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
    print("Terima kasih telah menggunakan ATM ini. Jangan lupa untuk mengambil kartu Anda.")
