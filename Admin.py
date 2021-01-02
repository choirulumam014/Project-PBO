import sqlite3
import Connect

class Login(Connect.Data_DB):
    def LoginAdmin(self):
        Connect.Data_DB()
        print("Selamat Datang Admin")
        Username = str(input("Masukkan Username Anda"))
        Password = str(input("Masukkan Password Anda"))
        query = 'SELECT * from data_admin WHERE username="{}" AND password="{}"'.format(Username, Password)
        self.Cursor.execute(query)
        if self.Cursor.fetchone() is not None:
            print ("Login Berhasil, Selamat Datang ", Username, " pada Fitur Admin.")
            MenuKaryawan().MenuAwal()
        else:
            print("Login Gagal")
            Login().LoginAdmin()
        self.ConDb.close()

class MenuKaryawan(Connect.Data_DB):
    def MenuAwal(self):
        Connect.Data_DB()
        MenuAwal=int(input(''' 
            Silahkan pilih :
        1. Tambah Data Karyawan
        2. Hapus Data Karyawan
        3. Pilih Data Karyawan
        4. Update Data Karyawan
        5. Reset Absensi
        6. Update Gaji Karyawan
        0. Kembali
        Masukkan Pilihan Menu: 
        '''))
        if MenuAwal == 1:
            MenuKaryawan().TambahData()
        elif MenuAwal == 2:
            MenuKaryawan().HapusData()
        elif MenuAwal == 3:
            MenuKaryawan().PilihData()
        elif MenuAwal == 4:
            MenuKaryawan().UpdateData()
        elif MenuAwal == 5:
            MenuKaryawan().ResetData()
        elif MenuAwal == 6:
            MenuKaryawan().Gaji()
        else:
            Login().LoginAdmin()
            
    def TambahData(self):
        NIP = str(input("Masukkan NIP Yang ingin ditambahkan :"))
        NamaKaryawan = str(input("Masukkan Nama :"))
        JenisKelamin = str(input("Masukkan Jenis Kelamin :"))
        Tanggal = str(input("Masukkan Tanggal Lahir (dd-mm-yyyy) :"))
        Alamat = str(input("Masukkan Alamat :"))
        Nomor = str(input("Masukkan Nomor Telphone :"))
        query = "INSERT INTO data_karyawan (NIP, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telphone) VALUES(?, ?, ?, ?, ?, ?)"
        Data = (NIP, NamaKaryawan, JenisKelamin, Tanggal, Alamat, Nomor)
        self.Cursor.execute(query, Data)
        self.ConDb.commit()
        self.ConDb.close()
        print("Data Berhasil Ditambahkan")
        MenuKaryawan().MenuAwal()
    
    def HapusData(self):
        DataHapus = str(input("Masukkan Nomor Induk Pegawai"))
        query = "DELETE FROM data_karyawan WHERE NIP = ?"
        Data = (DataHapus,)
        self.Cursor.execute(query, Data)
        self.ConDb.commit()
        self.ConDb.close()
        print("Data ", DataHapus, " berhasil dihapus")
        MenuKaryawan().MenuAwal()

    def ResetData(self):
        DataHapus = int(input("Tekan 1, Jika Ingin Mereset Data Absensi"))
        if DataHapus == 1:
            query = "DELETE FROM data_absensi"
            self.Cursor.execute(query)
            self.ConDb.commit()
            self.ConDb.close()
            print("Data berhasil Direset")
        else:
            ("Proses Dihentikan")
        MenuKaryawan().MenuAwal()

    def PilihData(self):
        Cari = str(input("Silahkan Masukkan Nomor Induk Pegawai"))
        query = "SELECT * from data_karyawan where NIP = ?"
        Data = (Cari,)
        self.Cursor.execute(query, Data)
        print (self.Cursor.fetchall())
        self.ConDb.close()
        MenuKaryawan().MenuAwal()

    def UpdateData(self):
        NIP = str(input("Masukkan NIP data yang ingin diubah:"))
        NamaKaryawan = str(input("Masukkan Nama :"))
        JenisKelamin = str(input("Masukkan Jenis Kelamin :"))
        Tanggal = str(input("Masukkan Tanggal (dd-mm-yyyy):"))
        Alamat = str(input("Masukkan Alamat :"))
        Nomor = str(input("Masukkan Nomor Telphone:"))
        query = "UPDATE data_karyawan SET nama_karyawan = ?, jenis_kelamin = ?, tanggal_lahir = ?, alamat = ?, no_telphone = ? WHERE NIP = ?"       
        Data = (NamaKaryawan, JenisKelamin, Tanggal, Alamat, Nomor, NIP)
        self.Cursor.execute(query, Data)
        self.ConDb.commit()
        self.ConDb.close()
        print("Data Berhasil Diubah")
        MenuKaryawan().MenuAwal()

    def Gaji (self):
        Connect.Data_DB
        Username = str(input("Masukkan NIP yang akan DiUpdate"))
        query = "SELECT Count(*)*250000 From data_absensi WHERE NIP = ?"
        Data = (Username,)
        self.Cursor.execute(query, Data)
        Gaji = self.Cursor.fetchall()[0][0]
        print(Gaji)
        self.ConDb.close()
        MenuKaryawan().UpdateGaji(Username,Gaji)

    def UpdateGaji(self,Username,Gaji):
        Connect.Data_DB
        query = "UPDATE data_penggajian SET jumlah_gaji = ? Where NIP = ?"
        Data = (Gaji, Username)
        self.Cursor.execute(query, Data)
        self.ConDb.commit()
        self.ConDb.close()
        MenuKaryawan().MenuAwal()