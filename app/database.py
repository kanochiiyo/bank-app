import json

class Database:
    def __init__(self, db:str = 'database-todo.txt'):
        self.db:str = db

    def insert(self, data: dict):
        with open(self.db, 'a') as file: # buka file
            data = json.dumps(data) # mengubah data jadi string agar bisa diterima oleh file txt
            file.write(data) # menuliskan ke dalam file pada akhir baris
            file.write("\n")

    def read(self):
        data: list = []
        with open(self.db) as file: 
            for line in file.readlines(): # membaca isi data baris per baris
                item = line.strip() # menghapus whitespace
                item = json.loads(item) # mengubah string jadi dictionary
                data.append(item) # menambahkan ke array

        return data