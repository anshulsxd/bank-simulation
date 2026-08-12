import time
print("-==-Bank simulation-==-")
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
            username=input("Enter Username: ")
            passw=input("Create Password: ")
            balance=input("Enter Starting Balance: ")

            with open("data.txt", "r") as f:
                for line in f:
                    existing_username=line.strip().split(",")[0]
                    if existing_username==username:
                        print("\nUsername already exist :(")
                        return
            
            with open("data.txt", "a") as f:
                f.write(username + "," + passw + "," + balance + "\n")

            print("\nUser Created successfully!")

        create_user()
    
    elif choice==2:
        def delete_user():
            input_username=input("Enter Username to delete: ")
            input_pass=input("Enter user's password: ")
            found=False
            updated_line=[]

            with open("data.txt", "r") as f:
                for line in f:
                    username, password, balance = line.strip().split(",")

                    if input_username==username and input_pass==password:
                        found=True
                        continue
                    updated_line.append(line)
            
            if not found:
                print("Username or password incorrect!")

            elif found:
                with open("data.txt", "w") as f:
                    f.writelines(updated_line)
                    print("User deleted successfully!")

        delete_user()
    
    elif choice==3:
        def check_balance():
            input_username=input("Enter Username: ")
            input_pass=input("Enter password: ")
            found=False

            with open("data.txt", "r") as f:
                for line in f:
                    username, password, balance = line.strip().split(",")

                    if input_username==username and input_pass==password:
                        found=True
                        print("\nFeatching Bank Balance...")
                        time.sleep(4)
                        print(f"\n{username}, your bank balance is {balance}")

            if not found:
                print("Username or password incorrect!")

        check_balance()

    elif choice==4:
        def update_balance():
            input_username=input("Enter Username: ")
            input_pass=input("Enter password: ")
            amount=int(input("Enter amount (+/-): "))

            found=False
            updated_line=[]

            with open("data.txt", "r") as f:
                for line in f:
                    username, password, balance = line.strip().split(",")

                    balance=int(balance)

                    if input_username==username and input_pass==password:
                        balance += amount
                        found=True

                    updated_line.append(f"{username},{password},{balance}\n")

            if not found:
                print("Invalid Username or password!")
                return
            elif found:
                with open("data.txt", "w") as f:
                    f.writelines(updated_line)
                print("\nBalance updated successfully!")
        
        update_balance()

    elif choice==5:
        def change_userORpassw():
            input_username=input("Enter Username: ")
            input_pass=input("Enter password: ")

            found=False

            with open("data.txt", "r") as f:
                lines = f.readlines()

            for i, line in enumerate(lines):
                username, password, balance = line.strip().split(",")

                if input_username==username and input_pass==password:
                    found=True
                    print("What you want to change?")
                    print("\n1. Username")
                    print("\n2. Password")
                    ch=int(input("Enter your choice: "))
                    if ch==1:
                        new_username=input("Enter new username: ")
                        lines[i] = f"{new_username},{password},{balance}\n"
                        print("Username changed successfully!")
                    elif ch==2:
                        new_pass=input("Enter new password: ")
                        lines[i] = f"{username},{new_pass},{balance}\n"
                        print("Password changed successfully!")
                    else:
                        print("Invalid choice!")
                    break

            if not found:
                print("\nUsername or password incorrect!")
                return

            with open("data.txt", "w") as f:
                f.writelines(lines)

        change_userORpassw()

    elif choice==6:
        print("Quiting Bank Simulation...")
        time.sleep(5)
        break

    else:
        print("Invalid option...")
