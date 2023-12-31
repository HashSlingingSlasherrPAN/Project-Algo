import os
import pandas as pd

def clear_console():
        os.system('cls')

def Header():
    with open('Header.txt','r') as header:
        header = header.read()
        print(header)

def Login_pengguna():
    def Register():
        regist =[input('Masukan Nama Anda\t:'),
                input('Masukkan Pekerjaan Anda\t:'),
                input('Masukkan Username\t:'),
                input('Masukkan Password\t:')]
        with open('login.csv','w') as register:
            user_data = f"{regist[0]},{regist[1]},{regist[2]},{regist[3]}"
            register.write(user_data)
        register.close()
        yakin_tidak = input('Apakah anda yakin? (y/t):')
        if yakin_tidak == 'y':
            print('Username dan Password tersimpan')
            input('enter untuk melanjutkan')
        else:
            Register()

    def login_user(username,password):
        with open('login.csv','r') as file:
            data = file.read()
            data = data.split(',')
            if username == data[2] and password == data[3]:
                print('Login Berhasil')
                input('enter untuk melanjutkan..')
                Menu_Awal()
            else:
                print('Login Gagal')
                input('Enter untuk login ulang')
                Login_pengguna()

    def ganti_userpass():
        clear_console()
        check =[input('Masukkan Username Lama :'),
                input('Masukkan Password Lama :')]
        with open('login.csv','r') as file:
            data_user = file.read()
            data_user = data_user.split(',')
            if check[0] == data_user[2] and check[1] == data_user[3]:
                akun_baru = [input('Masukkan Username baru :'),
                            input('Masukkan Password baru :')]
                with open('login.csv','w') as user_baru:
                    simpan_baru = f'{data_user[0]},{data_user[1]},{akun_baru[0]},{akun_baru[1]}'
                    user_baru.write(simpan_baru)
            else:
                print('Username atau Password yang anda masukkan salah')
                print('1. Kembali ke login')
                print('2. Ulangi mengubah akun')
                pilihan_ubah = int(input('Ketikkan pilihan anda :'))
                match pilihan_ubah:
                    case 1:
                        exit
                    case 2:
                        ganti_userpass()
                    case _ :
                        pass

    
    with open('login.csv','r') as lihat:
        a = len(lihat.readlines())
        if a == 0:
            with open('Tampilan Register.txt','r') as registers:
                register_gui = registers.read()
                print(register_gui)
            Register()
        else:
            clear_console()
            with open('Tampilan Login.txt','r') as gui:
                first_gui = gui.read()
                print(first_gui)
            with open('login.csv','r') as welcomings:
                welcoming = welcomings.read()
                Profil_Pengguna = welcoming.split(',')
                welcome = f"{'Selamat Datang'} {Profil_Pengguna[0]}"
                print(f"{welcome:^68}")
            pilihan_awal = (input('Ketikkan Pilihan Anda\t:'))
            match pilihan_awal:
                case '1' :
                    username_login = [input('Masukkan Username\t:'),input('Password \t\t:')]
                    login_user(username_login[0],username_login[1])
                case '2' :
                    ganti_userpass()
                case '3' :
                    clear_console()
                    exit
                case _ :
                    pass

def Menu_Awal():
    clear_console()
    with open('Menu Awal.txt','r') as gui_menu:
        gui_menu = gui_menu.read()
        print(gui_menu)
        pilihan_menu = input('Ketikkan Pilihan Anda :')
        match pilihan_menu:
            case '1' :
                Fitur_Pencatatan()
            case '2' :
                #Laporan Transaksi -- SOON ---
                pass
            case '3' :
                Menu_Hapus_Tambah_Kategori()
                pass
            case '4' :
                profil_pengguna()
            case '5' :
                Login_pengguna()

def profil_pengguna():
    clear_console()
    Header()
    with open('login.csv','r') as profil:
        profil = profil.read()
        profil = profil.split(',')
        Nama = f"Nama : {profil[0]}"
        Pekerjaan = f"Pekerjaan : {profil[1]}"
        print(f"{'=-=-=-=-=-=Profil=-=-=-=-=-=':^68}")
        print(f"{Nama:^68}")
        print(f"{Pekerjaan:^68}")
    input('Enter untuk kembali ke menu')
    Menu_Awal()

def Fitur_Pencatatan():
    clear_console()
    def Kategori_transaksi():
        kategori_kategori = pd.read_csv('Data kategori.csv' )
        print(kategori_kategori)
    def Catat_Debit():
            clear_console()
            Header()
            print(f"{'CATAT DEBIT':^68}")
            Debit = [
                    input('Masukkan Nama Transaksi :'),
                    Kategori_transaksi(),
                    input('Masukkan Tipe Transaksi :'),
                    input('Masukkan Nominal Transaksi :')]  
            tambah_debit = f"{Debit[0]},{Debit[2]},{Debit[3]}\n"

            with open('Data Debit.csv','a') as debit:
                debit.write(tambah_debit)
            debit.close()
            print('Berhasil disimpan!')
            input('enter untuk melanjutkan...')
            tambah_lagi = input('Tambah lagi? y/t:')
            if tambah_lagi == 'y':
                Catat_Debit()
            else:
                Fitur_Pencatatan()

    def Catat_Kredit():
            clear_console()
            Header()
            print(f"{'CATAT KREDIT':^68}")
            Kredit = [
                    input('Masukkan Nama Transaksi :'),
                    Kategori_transaksi(),
                    input('Masukkan Tipe Transaksi :'),
                    input('Masukkan Nominal Transaksi :')]  
            tambah_kredit = f"{Kredit[0]},{Kredit[2]},{Kredit[3]}\n"

            with open('Data Kredit.csv','a') as kredit:
                kredit.write(tambah_kredit)
            kredit.close()
            print('Berhasil disimpan!')
            input('enter untuk melanjutkan...')
            tambah_lagi = input('Tambah lagi? y/t:')
            if tambah_lagi == 'y':
                Catat_Kredit()
            else:
                Fitur_Pencatatan()
    def Catat_Utang():
            clear_console()
            Header()
            print(f"{'CATAT UTANG':^68}")
            utang = [
                    input('Masukkan Nama Transaksi :'),
                    Kategori_transaksi(),
                    input('Masukkan Tipe Transaksi :'),
                    input('Masukkan Nominal Transaksi :')]  
            tambah_utang = f"{utang[0]},{utang[2]},{utang[3]}\n"

            with open('Data Utang.csv','a') as utang:
                utang.write(tambah_utang)
            utang.close()
            print('Berhasil disimpan!')
            input('enter untuk melanjutkan...')
            tambah_lagi = input('Tambah lagi? y/t:')
            if tambah_lagi == 'y':
                Catat_Utang()
            else:
                Fitur_Pencatatan()

    clear_console()
    with open('GUI Catat.txt','r') as pilihan_catat:
        pilih_fitur = pilihan_catat.read()
        print(pilih_fitur)
    pilihan_fitur = input('Masukkan Pilihan Anda :')
    match pilihan_fitur:
        case '1' :
            Catat_Debit()
        case '2' :
            Catat_Kredit()
        case '3' :
            Catat_Utang()
        case '4' :
            Menu_Hapus_Tambah_Kategori()
        case '5' :
            Menu_Awal()
        case _ :
            pass

def Menu_Hapus_Tambah_Kategori():
    def Menu_Kelola():
        clear_console()
        with open('Hapus Kategori.txt','r') as gui_cat:
            gui_cat = gui_cat.read()
            print(gui_cat)
        pilhan_add_del = input('Pilihan Anda :')
        match pilhan_add_del:
            case '1' :
                Tambah_Kategori()
            case '2' :
                hapus_kategori()
            case '3' :
                Fitur_Pencatatan()
            case _ :
                Menu_Hapus_Tambah_Kategori()

    def Tambah_Kategori():
        clear_console()
        Header()
        frame_cat = pd.read_csv('Data kategori.csv')
        print(frame_cat)
        tambah_kategori = input('Ketikkan Kategori Baru :')
        tambah_kategori = {'Kategori' : tambah_kategori}
        panjang_index = len(frame_cat)
        frame_cat.loc[panjang_index] =  tambah_kategori
        frame_cat.to_csv('Data kategori.csv', index= False)
        print(frame_cat)
        pilihan_cat = input('kategori telah ditambah.. buat kategori baru lagi? y/t :')
        if pilihan_cat == 'y':
            Tambah_Kategori()
        else:
            Menu_Hapus_Tambah_Kategori()

    def hapus_kategori():
        clear_console()
        Header()
        frame_cat = pd.read_csv('Data kategori.csv')
        print(frame_cat)
        panjang_index = len(frame_cat)
        print("Ketikkan Nomor Urut Kategori Untuk Menghapus ")
        print("Apabila Batal Ketik 't' untuk Batal ")
        hapus_cat = input('Kategori yg akan dihapus :')
        hapus_cat_str = str(hapus_cat)
        match hapus_cat_str:
            case 't':
                Menu_Hapus_Tambah_Kategori()
            case _ :
                if int(hapus_cat) <= panjang_index-1:
                    frame_cat = frame_cat.drop(int(hapus_cat))
                    frame_cat.index = range(0,len(frame_cat))
                else:
                    print('Pilihan diluar jangkauan..')
                    input('enter untuk mengulang')
                    hapus_kategori()
                print(frame_cat)
                print('Hapus Lagi? y/t')
                hapus_cat_lagi = input('Pilihan Anda :')
                match hapus_cat_lagi:
                    case 'y':
                        hapus_kategori()
                    case 't':
                        Menu_Hapus_Tambah_Kategori()
                    case _ :
                        Menu_Hapus_Tambah_Kategori()
    
    Menu_Kelola()


        
Login_pengguna()
# profil_pengguna()
# Fitur_Pencatatan()