global kartu
kartu = ["Rick Sanchez", 61869, 123456, 1000000, 0]
def menudeposito():
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
            menudeposito()
        else:
            print("Anda sudah memiliki rekening deposito.")
            menudeposito()

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
            menudeposito()
        else:
            print("Silakan membuka rekening deposito terlebih dahulu.")
            menudeposito()

    if(Menu == 3):
        if(Punya_deposito == True):
            print("Anda tidak dapat mencairkan deposito pada saat yang sama dengan periode pembukaan rekening deposito Anda.")
            menudeposito()
        else:
            print("Silakan membuka rekening deposito terlebih dahulu.")
            menudeposito()

    if(Menu == 4):
        print("", end='')

menudeposito()