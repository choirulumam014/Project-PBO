import sqlite3
import Connect
import Pengguna
import Divisi

ConDb = sqlite3.connect('gajikaryawan.db')
Cursor = ConDb.cursor()

#Admin
def TambahData():
    Username = str(input("Masukkan Username Sementara "))
    Password = str(input("Masukkan Password Sementara "))
    NIP = str(input("Masukkan NIP :"))
    Nama = str(input("Masukkan Nama :"))
    Jenis_Kelamin = str(input("Masukkan Jenis Kelamin :"))
    Tanggal = str(input("Masukkan Tanggal Lahir (dd-mm-yyyy) :"))
    Alamat = str(input("Masukkan Alamat :"))
    Telphone = str(input("Masukkan Nomor Telphone :"))
    Value = Pengguna.Karyawan(Username,Password,NIP,Nama,Jenis_Kelamin,Tanggal,Alamat,Telphone)
    query ='INSERT INTO data_karyawan (NIP, nama_karyawan, jenis_kelamin, tanggal_lahir, alamat, no_telphone) VALUES(?, ?, ?, ?, ?, ?)'
    Data = (Value.getNIP(), Value.getNama(), Value.getJenisKelamin(), Value.getTanggalLahir(), Value.getAlamat(), Value.getTelphone())
    Cursor.execute(query, Data)
    ConDb.commit()
    ConDb.close()
    print("Data Berhasil Ditambahkan")
    
def HapusData():
    Connect.Data_DB()
    DataHapus = str(input("Masukkan Nomor Induk Pegawai"))
    query = "DELETE FROM data_karyawan WHERE NIP = ?"
    Data = (DataHapus,)
    Cursor.execute(query, Data)
    ConDb.commit()
    ConDb.close()
    print("Data ", DataHapus, " berhasil dihapus")

def ResetData():
    Connect.Data_DB()
    DataHapus = int(input("Tekan 1, Jika Ingin Mereset Data Absensi"))
    if DataHapus == 1:
        query = "DELETE FROM data_absensi"
        Cursor.execute(query)
        ConDb.commit()
        ConDb.close()
        print("Data berhasil Direset")
    else:
        ("Proses Dihentikan")

def PilihData():
    Connect.Data_DB()
    Cari = str(input("Silahkan Masukkan Nomor Induk Pegawai"))
    query = "SELECT * from data_karyawan where NIP = ?"
    Data = (Cari,)
    Cursor.execute(query, Data)
    print (Cursor.fetchall())
    ConDb.close()

def UpdateData():
    Connect.Data_DB()
    Username = None
    Password = None
    NIP = str(input("Masukkan NIP yang akan diubah :"))
    Nama = str(input("Masukkan Nama :"))
    Jenis_Kelamin = str(input("Masukkan Jenis Kelamin :"))
    Tanggal = str(input("Masukkan Tanggal Lahir (dd-mm-yyyy) :"))
    Alamat = str(input("Masukkan Alamat :"))
    Telphone = str(input("Masukkan Nomor Telphone :"))
    Value = Pengguna.Karyawan(Username,Password,NIP,Nama,Jenis_Kelamin,Tanggal,Alamat,Telphone)
    query = "UPDATE data_karyawan SET username = ?, password = ? nama_karyawan = ?, jenis_kelamin = ?, tanggal_lahir = ?, alamat = ?, no_telphone = ? WHERE NIP = ?"       
    Data = (Value.getNIP(), Value.getNama(), Value.getJenisKelamin(), Value.getTanggalLahir(), Value.getAlamat(), Value.getTelphone())
    Cursor.execute(query, Data)
    ConDb.commit()
    ConDb.close()
    print("Data Berhasil Diubah")

#Karyawan
def Biodata():
    Connect.Data_DB
    NIP = str(input("Masukkan NIP Anda")) 
    query = "SELECT * from data_karyawan where NIP = ?"
    Data = (NIP,)
    Cursor.execute(query, Data)
    print (Cursor.fetchall())
    ConDb.close()

def Rekam():
    Connect.Data_DB
    NIP = str(input("Masukkan NIP Anda"))
    query = "SELECT Count(*) From data_absensi WHERE NIP = ?"
    Data = (NIP,)
    Cursor.execute(query,Data)
    print ("Anda Bekerja Sebanyak", Cursor.fetchall()[0][0], "Hari")
    ConDb.close()
    
def Gaji ():
    Connect.Data_DB
    NIP = str(input("Masukkan NIP Anda"))
    query = "SELECT jumlah_gaji From data_penggajian WHERE NIP = ?"
    Data = (NIP,)
    Cursor.execute(query, Data)
    Gaji = Cursor.fetchall()[0][0]
    print(Gaji)
    ConDb.close()

def AmbilGaji():
    Connect.Data_DB
    NIP = str(input("Masukkan NIP Anda"))
    Ambil = int(input("Berapa banyak uang yang ingin anda ambil ?"))
    query = "SELECT jumlah_gaji From data_penggajian WHERE NIP = ?"
    Data = (NIP,)
    Cursor.execute(query, Data)
    Sisa = Cursor.fetchall()[0][0] - Ambil
    print("Anda telah berhasil mengambil uang sebanyak Rp.", Ambil)
    print("Sisa Gaji Anda Sebanyak Rp", Sisa)
    query1 = "UPDATE data_penggajian SET jumlah_gaji = ? Where NIP = ?"
    Data1 = (Sisa, NIP)
    Cursor.execute(query1, Data1)
    ConDb.commit()
    ConDb.close()
        
def Absensi():
    Connect.Data_DB
    NIP = str(input("Masukkan NIP Anda"))
    absen = str(input("Gunakan angka 1 untuk Absensi "))
    query = "INSERT INTO data_absensi (kehadiran,NIP) VALUES(?, ?)"
    Data = (absen, NIP)
    Cursor.execute(query, Data)
    print ("Selamat Anda Berhasil Melakukan absensi")
    ConDb.commit()
    ConDb.close()
    
def GantiPW():
    Connect.Data_DB 
    NIP = str(input("Masukkan NIP Anda"))
    Username = str(input("Masukkan Username Baru"))
    Password = str(input("Masukkan Password Baru"))
    Nama = None
    Jenis_Kelamin = None
    Tanggal_Lahir = None
    Alamat = None
    Telphone = None
    Value = Pengguna.Karyawan(Username,Password,NIP,Nama,Jenis_Kelamin,Tanggal_Lahir,Alamat,Telphone)
    query = "UPDATE data_karyawan SET username = ?, password = ? where NIP = ?"
    Data = (Value.getUsername(), Value.getPassword(), Value.getNIP())
    Cursor.execute(query, Data)
    ConDb.commit()
    ConDb.close()
    print("Selamat, Password Anda Telah Diubah")

#Manager
def TambahDivisi():
    Connect.Data_DB()
    IdDivisi = None
    Jabatan = str(input("Masukkan Jabatan Baru :"))
    Gaji_Pokok = str(input("Masukkan Nominal :"))
    Tunjangan = str(input("Masukkan Nominal :"))
    Value = Divisi.Divisi(IdDivisi,Jabatan, Gaji_Pokok, Tunjangan)
    query = "INSERT INTO data_divisi (jabatan, gaji_pokok, tunjangan) VALUES(?, ?, ?)"
    Data = (Value.getJabatan(), Value.getGajiPokok(), Value.getTunjangan())
    Cursor.execute(query, Data)
    ConDb.commit()
    ConDb.close()
    print("Data Berhasil Ditambahkan")


def UpdateDivisi():
    Connect.Data_DB()
    IdDivisi = None
    Jabatan = str(input("Masukkan Jabatan yang Dipilih :"))
    Gaji_Pokok = str(input("Masukkan Nominal :"))
    Tunjangan = str(input("Masukkan Nominal :"))
    Value = Divisi.Divisi(IdDivisi,Jabatan, Gaji_Pokok, Tunjangan)
    query = "UPDATE data_divisi SET gaji_pokok = ?, tunjangan = ? WHERE jabatan = ?"       
    Data = ( Value.getGajiPokok(), Value.getTunjangan(),Value.getJabatan())
    Cursor.execute(query, Data)
    ConDb.commit()
    ConDb.close()
    print("Data Berhasil Diubah")


def HapusDivisi():
    Connect.Data_DB()
    DataHapus = str(input("Masukkan Jabatan yang Dihapus"))
    query = "DELETE FROM data_devisi WHERE jabatan = ?"
    Data = (DataHapus,)
    Cursor.execute(query, Data)
    ConDb.commit()
    ConDb.close()
    print("Data ", DataHapus, " berhasil dihapus")


def GajiDivisi ():
    Connect.Data_DB
    NIP = str(input("Masukkan NIP :"))
    query = "SELECT Count(*) From data_absensi WHERE NIP = ?"
    Data = (NIP,)
    Cursor.execute(query, Data)
    Absen = Cursor.fetchall()[0][0]
    query1 = "SELECT gaji_pokok From data_divisi WHERE NIP = ?"
    Data1 = (NIP,)
    Cursor.execute(query1, Data1)
    Pokok = Cursor.fetchall()[0][0]
    query2 = "SELECT tunjangan From data_divisi Where NIP = ?"
    Data2 = (NIP,)
    Cursor.execute(query2, Data2)
    Tunjangan = Cursor.fetchall()[0][0]
    Gaji = Absen * Pokok + Tunjangan
    print(Gaji)
    query3 = "UPDATE data_penggajian SET jumlah_gaji = ? Where NIP = ?"
    Data3 = (Gaji, NIP)
    Cursor.execute(query3, Data3)
    ConDb.commit()
    ConDb.close()

GajiDivisi()