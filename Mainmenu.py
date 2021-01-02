import sqlite3
import Admin
import Karyawan
import Connect

class MenuUtama:
    def Menu(self):
        Connect.Data_DB()
        pilihan = int(input('''
        Selamat datang di Toko Kelontong Jaya Baru
        1. Admin
        2. Karyawan
        '''))
        if pilihan == 1:
            Admin.Login().LoginAdmin()
        elif pilihan == 2:
            Karyawan.Login().LoginKaryawan()
        else :
            print("Maaf Pilihan Anda Tidak Tersedia")

MenuUtama().Menu()