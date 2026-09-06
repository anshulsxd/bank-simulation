import time
import hashlib
import os
import json
print("-==-Bank simulation-==-")
DATA_FILE = "data.json"

def ensure_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({}, f)

def load_data():
    ensure_data_file()
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
while True:
    print("\nChoose an option:")
    print("\n1. Add user")
    print("\n2. Delete user")
    print("\n3. Check balance")
    print("\n4. Update balance")
    print("\n5. Change Username/Password")
    print("\n6. Exit")

    choice=int(input("\nEnter your choice: "))


    if choice==1:
        def create_user():
            username = input("Enter Username: ")
            passw = input("Create Password: ")
            hashed_pw = hashlib.sha256(passw.encode()).hexdigest()
            balance = input("Enter Starting Balance: ")

            # validate balance
            try:
                balance_val = int(balance)
            except ValueError:
                print("Invalid starting balance. Use an integer.")
                return

            data = load_data()
            if username in data:
                print("Username already exist :(")
                return

            data[username] = {"password": hashed_pw, "balance": balance_val}
            save_data(data)
            print("\nUser Created successfully!")

        create_user()
    
    elif choice==2:
        def delete_user():
            input_username=input("Enter Username to delete: ")
            input_pass=input("Enter user's password: ")
            hashed_pw=hashlib.sha256(input_pass.encode()).hexdigest()

            data = load_data()
            if input_username not in data or data[input_username].get("password") != hashed_pw:
                print("Username or password incorrect!")
                return

            del data[input_username]
            save_data(data)
            print("User deleted successfully!")

        delete_user()
    
    elif choice==3:
        def check_balance():
            input_username=input("Enter Username: ")
            input_pass=input("Enter password: ")
            hashed_pw=hashlib.sha256(input_pass.encode()).hexdigest()

            data = load_data()
            user = data.get(input_username)
            if not user or user.get("password") != hashed_pw:
                print("Username or password incorrect!")
                return

            balance = user.get("balance", 0)
            print("\nFeatching Bank Balance...")
            time.sleep(2)
            print(f"\n{input_username}, your bank balance is {balance}")

        check_balance()

    elif choice==4:
        def update_balance():
            input_username=input("Enter Username: ")
            input_pass=input("Enter password: ")
            hashed_pw=hashlib.sha256(input_pass.encode()).hexdigest()
            try:
                amount=int(input("Enter amount (+/-): "))
            except ValueError:
                print("Invalid amount. Use an integer.")
                return

            data = load_data()
            user = data.get(input_username)
            if not user or user.get("password") != hashed_pw:
                print("Invalid Username or password!")
                return

            try:
                curr = int(user.get("balance", 0))
            except ValueError:
                curr = 0

            curr += amount
            data[input_username]["balance"] = curr
            save_data(data)
            print("\nBalance updated successfully!")
        
        update_balance()

    elif choice==5:
        def change_userORpassw():
            input_username=input("Enter Username: ")
            input_pass=input("Enter password: ")
            hashed_pw=hashlib.sha256(input_pass.encode()).hexdigest() # current pw as hash

            data = load_data()
            user = data.get(input_username)
            if not user or user.get("password") != hashed_pw:
                print("\nUsername or password incorrect!")
                return

            print("What you want to change?")
            print("\n1. Username")
            print("\n2. Password")
            ch=int(input("Enter your choice: "))
            if ch==1:
                new_username=input("Enter new username: ")
                if new_username in data:
                    print("Username already exist :(")
                    return
                data[new_username] = data.pop(input_username)
                print("Username changed successfully!")
            elif ch==2:
                new_pass=input("Enter new password: ")
                new_hashed_pw=hashlib.sha256(new_pass.encode()).hexdigest() # new pass as hash
                data[input_username]["password"] = new_hashed_pw
                print("Password changed successfully!")
            else:
                print("Invalid choice!")
                return

            save_data(data)
        change_userORpassw()

    elif choice==6:
        print("Quiting Bank Simulation...")
        break

    else:
        print("Invalid option...")