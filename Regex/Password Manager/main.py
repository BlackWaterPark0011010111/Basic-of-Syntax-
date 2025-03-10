import password_utils
import storage

def main():
    passwords = storage.load_passwords()

    while True:
        print("\nPassword Manager")
        print("1. Create a password")
        print("2. Check my password")
        print("3. Just show all saved")
        print("4. Exit")

        choice = input("Choose ure action: ").strip()
        
        if choice == "1":
            site = input("Enter a website name: ").strip()
            password = password_utils.generate_password()
            hashed_password = password_utils.hash_password(password)
            passwords[site] = hashed_password
            storage.save_passwords(passwords)
            print(f"geretation password for: {site}: {password}")
        
        elif choice == "2":
            site = input("enter a website name: ").strip()
            if site in passwords:
                entered_password = input("Введите пароль: ")
                if password_utils.verify_password(entered_password, passwords[site]):
                    print("password is correct!")
                else:
                    print("Wrong password!")
            else:
                print("heres no saved password 4 this website.")

        elif choice == "3":
            if passwords:
                print("Heres ure saved passwords:")
                for site in passwords:
                    print(f"- {site}")
            else:
                print("here`s no saved passwords.")

        elif choice == "4":
            print("Exit...")
            break

        else:
            print("wrong, Try again.")

if __name__ == "__main__":
    main()