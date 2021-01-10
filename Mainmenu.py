import sqlite3
import Pelaksana
import Connect
import os
from abc import ABC, abstractmethod
from getpass import getpass

os.system('cls' if os.name == 'nt' else 'clear')

class Masuk:
    def LoginMaganer(self):
        pass

    def LoginAdmin(self):
        pass

    def LoginKaryawan(self):
        pass

class Menu:
    def MenuUtama(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        pilihan = int(input('''
        Selamat datang Di PT Mencari Cinta Abadi
        1. Manager
        2. Admin
        3. Karyawan
        '''))
        if pilihan == 1:
            Login().LoginManager()
        elif pilihan == 2 :
            Login().LoginAdmin()
        elif pilihan == 3:
            Login().LoginKaryawan()
        else :
            print("Maaf Pilihan Anda Tidak Tersedia")

    def MenuManager(self):
        pilihan = int(input('''
            Menu Manager :
        1. Tambahan Divisi
        2. Update Data
        3. Hapus Divisi
        4. Update Gaji
        0. Kembali
        '''))
        if pilihan == 1:
            Pelaksana.TambahDivisi()
            Menu().MenuUtama()
        elif pilihan == 2:
            Pelaksana.UpdateDivisi()
            Menu().MenuUtama()
        elif pilihan == 3:
            Pelaksana.HapusDivisi()
            Menu().MenuUtama()
        elif pilihan == 4:
            Pelaksana.GajiDivisi()
            Menu().MenuUtama()
        else:
            Menu().MenuUtama()

    def MenuAdmin(self):
        Pilihan=int(input(''' 
            Menu Admin :
        1. Tambah Data Karyawan
        2. Hapus Data Karyawan
        3. Pilih Data Karyawan
        4. Update Data Karyawan
        5. Reset Absensi
        0. Kembali
        Masukkan Pilihan Menu: 
        '''))
        if Pilihan == 1:
            Pelaksana.TambahData()
            Menu().MenuUtama()
        elif Pilihan == 2:
            Pelaksana.HapusData()
            Menu().MenuUtama()
        elif Pilihan == 3:
            Pelaksana.PilihData()
            Menu().MenuUtama()
        elif Pilihan == 4:
            Pelaksana.UpdateData()
            Menu().MenuUtama()
        elif Pilihan == 5:
            Pelaksana.ResetData()
            Menu().MenuUtama()
        else:
            Menu().MenuUtama()

    def MenuKaryawan(self):
        FiturKaryawan = int(input(''' 
            MENU Karyawan :
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
            Pelaksana.Biodata()
            Menu().MenuUtama()
        elif FiturKaryawan == 2 :
            Pelaksana.Rekam()
            Menu().MenuUtama()
        elif FiturKaryawan == 3:
            Pelaksana.Gaji()
            Menu().MenuUtama()
        elif FiturKaryawan == 4:
            Pelaksana.AmbilGaji()
            Menu().MenuUtama()
        elif FiturKaryawan == 5:
            Pelaksana.Absensi()
            Menu().MenuUtama()
        elif FiturKaryawan == 6:
            Pelaksana.GantiPW()
            Menu().MenuUtama()
        else:
            Menu().MenuUtama()

class Login(Connect.Data_DB):
    def LoginManager(self):
        print("Selamat Datang Manager")
        Username = str(input("Masukkan Username Anda"))
        Password = getpass("Masukkan Password")
        query = 'SELECT * from data_manager WHERE username="{}" AND password="{}"'.format(Username, Password)
        self.Cursor.execute(query)
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.Cursor.fetchone() is not None:
            print ("Login Berhasil, Selamat Datang ", Username, " pada Fitur Admin.")
            Menu().MenuManager()
        else:
            print("Login Gagal")
            Menu().MenuUtama()
        self.ConDb.close()

    def LoginAdmin(self):
        print("Selamat Datang Admin")
        Username = str(input("Masukkan Username Anda"))
        Password = getpass("Masukkan Password")
        query = 'SELECT * from data_admin WHERE username="{}" AND password="{}"'.format(Username, Password)
        self.Cursor.execute(query)
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.Cursor.fetchone() is not None:
            print ("Login Berhasil, Selamat Datang ", Username, " pada Fitur Admin.")
            Menu().MenuAdmin()
        else:
            print("Login Gagal")
            Menu().MenuUtama()
        self.ConDb.close()

    def LoginKaryawan(self):
        print("Selamat Datang Karyawan")
        Username = str(input("Masukkan Username"))
        Password = getpass("Masukkan Password")
        query = 'SELECT * from data_karyawan WHERE username="{}" AND password="{}"'.format(Username, Password)
        self.Cursor.execute(query)
        os.system('cls' if os.name == 'nt' else 'clear')
        if self.Cursor.fetchone() is not None:
            print ("Login Berhasil, Selamat Datang ", Username, " pada Fitur Admin.")
            Menu().MenuKaryawan()
        else:
            print ("Login Gagal")
            Menu().MenuUtama()
        self.ConDb.close()

Menu().MenuUtama()