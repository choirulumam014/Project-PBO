import sqlite3

class Data_DB:
    def __init__(self):
        self.ConDb = sqlite3.connect('gajikaryawan.db')
        self.Cursor = self.ConDb.cursor()