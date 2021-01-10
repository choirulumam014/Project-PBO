class Divisi:
    def __init__(self, id_Divisi, Jabatan, Gaji_Pokok, Tunjangan):
        self.__id_Divisi = id_Divisi
        self.__Jabatan = Jabatan
        self.__Gaji_Pokok = Gaji_Pokok
        self.__Tunjangan = Tunjangan

    def getIdDivisi(self):
        return self.__id_Divisi

    def setIdDivisi(self,id_Divisi):
        self.__id_Divisi = id_Divisi

    def getJabatan(self):
        return self.__Jabatan

    def setJabatan(self,Jabatan):
        self.__Jabatan = Jabatan

    def getGajiPokok(self):
        return self.__Gaji_Pokok

    def setGajiPokok(self,Gaji_Pokok):
        self.__Gaji_Pokok = Gaji_Pokok

    def getTunjangan(self):
        return self.__Tunjangan

    def setTunjangan(self,Tunjangan):
        self.__Tunjangan = Tunjangan

class Gaji:
    def __init__(self, Penggajian):
        self.__Penggajian = Penggajian
    
    def getGaji(self):
        return self.__Penggajian
    
    def setGaji(self,Penggajian):
        self.__Penggajian = Penggajian