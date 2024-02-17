from uuid import uuid4 # import file UUID bawaan py
from app.database import Database
import random

class BankAccount:
    def __init__(self):
        self.db_name = "bank-db.txt" # ngeset variabel db_name yang isinya adalah db txt
        self.database = Database(
            db = self.db_name
            ) 
        # inisiasi class Database dengan param db (db adalah var yg isinya self.db_Name)

    def get_random_account(self):
        return random.randint(
            1000000000, 9999999999
        )
    # mengembalikan random int number

    def create(self, full_name:str, pin:str):
        account = {
            "id": str(uuid4()), # membuat id baru secara unique
            "acc_no": str(
                self.get_random_account()
            ), # memanggil fungsi untuk ngegenerate no akun
            "full_name": full_name,
            "pin": pin,
            "balance": 0
        }

        self.database.insert(account) # manggil fungsi menambahkan data

        return account