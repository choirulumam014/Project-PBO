import sqlite3
import Connect

class Login(Connect.Data_DB):
    def LoginKaryawan(self):
        Connect.Data_DB()
        print("Selamat Datang Karyawan")
        Username = str(input("Masukkan Nomor Induk Pegawai Anda"))
        Password = str(input("Masukkan Password Anda"))
        query = 'SELECT * from data_karyawan WHERE NIP="{}" AND password="{}"'.format(Username, Password)
        self.Cursor.execute(query)
        if self.Cursor.fetchone() is not None:
            print ("Login Berhasil, Selamat Datang ", Username, " pada Fitur Admin.")
            Karyawan().FiturKaryawan(Username)
        else:
            print ("Login Gagal")
            Login().LoginKaryawan()
        self.ConDb.close()

class Karyawan (Connect.Data_DB):
    def FiturKaryawan(self,Username):
        Connect.Data_DB()
        FiturKaryawan = int(input(''' 
            MENU Member
        1. Tampilkan Data Diri
        2. Tampilkan Rekam Kerja
        3. Tampilan Gaji Karyawan
        4. Ambil Gaji
        5. Lakukan Absensi Kerja
        6. Edit Password
        0. Kembali
        Masukkan Pilihan Menu: 
        '''))
        if FiturKaryawan == 1 :
            Karyawan().Biodata(Username)
        elif FiturKaryawan == 2 :
            Karyawan().Rekam(Username)
        elif FiturKaryawan == 3:
            Karyawan().Gaji(Username)
        elif FiturKaryawan == 4:
            Karyawan().AmbilGaji(Username)
        elif FiturKaryawan == 5:
            Karyawan().Absensi(Username)
        elif FiturKaryawan == 6:
            Karyawan().GantiPW(Username)
        else:
            Login().LoginKaryawan()
        
    def Biodata(self, Username):
        Connect.Data_DB 
        query = "SELECT * from data_karyawan where NIP = ?"
        Data = (Username,)
        self.Cursor.execute(query, Data)
        print (self.Cursor.fetchall())
        self.ConDb.close()
        Karyawan().FiturKaryawan(Username)

    def Rekam(self,Username):
        Connect.Data_DB
        query = "SELECT Count(*) From data_absensi WHERE NIP = ?"
        Data = (Username,)
        self.Cursor.execute(query,Data)
        print ("Anda Bekerja Sebanyak", self.Cursor.fetchall(), "Hari")
        self.ConDb.close()
        Karyawan().FiturKaryawan(Username)
    
    def Gaji (self,Username):
        Connect.Data_DB
        query = "SELECT jumlah_gaji From data_penggajian WHERE NIP = ?"
        Data = (Username,)
        self.Cursor.execute(query, Data)
        Gaji = self.Cursor.fetchall()[0][0]
        print(Gaji)
        self.ConDb.close()
        Karyawan().FiturKaryawan(Username)

    def AmbilGaji(self,Username,):
        Connect.Data_DB
        Ambil = int(input("Berapa banyak uang yang ingin anda ambil ?"))
        query = "SELECT jumlah_gaji From data_penggajian WHERE NIP = ?"
        Data = (Username,)
        self.Cursor.execute(query, Data)
        Sisa = self.Cursor.fetchall()[0][0] - Ambil
        print("Anda telah berhasil mengambil uang sebanyak Rp.", Ambil)
        print("Sisa Gaji Anda Sebanyak Rp", Sisa)
        self.ConDb.close()
        Karyawan().UpdateGaji(Username,Sisa)

    def UpdateGaji(self,Username,Sisa):
        Connect.Data_DB
        query = "UPDATE data_penggajian SET jumlah_gaji = ? Where NIP = ?"
        Data = (Sisa, Username)
        self.Cursor.execute(query, Data)
        self.ConDb.commit()
        self.ConDb.close()
        Karyawan().FiturKaryawan(Username)
        
    def Absensi(self,Username):
        Connect.Data_DB
        absen = str(input("Gunakan angka 1 untuk Absensi "))
        query = "INSERT INTO data_absensi (kehadiran,NIP) VALUES(?, ?)"
        Data = (absen, Username)
        self.Cursor.execute(query, Data)
        print ("Selamat Anda Berhasil Melakukan absensi")
        self.ConDb.commit()
        self.ConDb.close()
        Karyawan().FiturKaryawan(Username)
    
    def GantiPW(self, Username):
        Connect.Data_DB 
        PWBaru = str(input("Masukkan Password Baru"))
        query = "UPDATE data_karyawan SET password = ? where NIP = ?"
        Data = (PWBaru, Username)
        self.Cursor.execute(query, Data)
        self.ConDb.commit()
        self.ConDb.close()
        print("Selamat, Password Anda Telah Diubah")
        Karyawan().FiturKaryawan(Username)