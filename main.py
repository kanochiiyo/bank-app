from app.bank_account import BankAccount

bank = BankAccount()

while True:
    print("Welcome to Bank App")

    print("1. Create new account")
    print("2. Go to system")

    option = input("Input your choice: ")

    if option == "1":
        full_name = input("Input your full name: ")
        pin = input("Input your pin number: ")

        data = bank.create(full_name, pin)

        print("Successful create your account! \n\n")
        print("----------------------------------------")
        print(f"Name: {data['full_name']}")
        print(f"Account number: {data['acc_no']}")
        print(f"Balance: {data['balance']}")
        print("----------------------------------------")
        print("\n\n")
    elif option == "2":
        pass
