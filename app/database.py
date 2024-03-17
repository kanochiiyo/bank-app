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

    def get_by_key(self, key:str, search_value:str):
        single_item: dict = None
        item_line = 0

        with open(self.db) as file:
            for line in file.readlines():
                item_line += 1
                item = line.strip()
                item = json.loads(item) # ubah string jadi dictionary

                if item.get(key) == search_value:
                    single_item = item.copy()
                    break
        return {"line": item_line, "data": single_item}
    
    def get_by_id(self, id:str):
        single_item:dict = None
        item_line = 0

        with open(self.db) as file:
            for line in file.readlines():
                item_line += 1
                item = line.strip()
                item = json.loads(item)

                if item.get("id") == search_value:
                    single_item = item.copy()
                    break
        return {"line": item_line, "data": single_item}
    
    def update(self, id:str, updated_data:dict):
        single_item:dict = self.get_by_id(id)

        if not single_item.get('data'):
            return False
        
        with open(self.db, 'r') as file:
            lines = file.readlines()
            lines[single_item['line'] - 1] = json.dumps(updated_data) + '\n' # menambahkan new line pada akhir baris

            with open(self.db, "w") as file:
                file.writelines(lines) # data disimpan dan tulis ulang

        return {"line": single_item.get('line'), "data": updated_data}

# get_by_key : mengambil data  dari tiap baris disesuaikan dengan key json yang sesuai. item.get(key) sifatnya dinamis
# get_by_id : mengambil data spesifik by id