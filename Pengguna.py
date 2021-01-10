class Pengguna:
    def __init__(self, Username, Password):
        self.__Username = Username
        self.__Password = Password

    def getUsername(self):
        return self.__Username

    def setUsername(self,Username):
        self.__Username = Username

    def getPassword(self):
        return self.__Password

    def setPassword(self,Password):
        self.__Password = Password

class Manager(Pengguna):
    def __init__(self, Username, Password, Nama):
        super().__init__(Username, Password)
        self.__Nama = Nama

    def getNama(self):
        return self.__Nama

class Admin(Pengguna):
    def __init__(self, Username, Password, Nama):
        super().__init__(Username, Password)
        self.__Nama = Nama

    def getNama(self):
        return self.__Nama
        
class Karyawan(Pengguna):
    def __init__(self,Username, Password, NIP, Nama, Jenis_Kelamin, Tanggal_Lahir, Alamat, Telphone):
        super().__init__(Username,Password)
        self.__NIP = NIP
        self.__Nama = Nama
        self.__Jenis_Kelamin = Jenis_Kelamin
        self.__Tanggal_Lahir = Tanggal_Lahir
        self.__Alamat = Alamat
        self.__Telphone = Telphone

    def getNIP(self):
        return self.__NIP

    def setNIP(self,NIP):
        self.__NIP = NIP  

    def getNama(self):
        return self.__Nama

    def setNama(self,Nama):
        self.__Nama = Nama

    def getJenisKelamin(self):
        return self.__Jenis_Kelamin

    def setJenisKelamin(self,Jenis_Kelamin):
        self.__Jenis_Kelamin = Jenis_Kelamin

    def getTanggalLahir(self):
        return self.__Tanggal_Lahir

    def setTanggalLahir(self,Tanggal_Lahir):
        self.__Tanggal_Lahir = Tanggal_Lahir

    def getAlamat(self):
        return self.__Alamat

    def setAlamat(self,Alamat):
        self.__Alamat = Alamat

    def getTelphone(self):
        return self.__Telphone

    def setTelphone(self,Telphone):
        self.__Telphone = Telphone
