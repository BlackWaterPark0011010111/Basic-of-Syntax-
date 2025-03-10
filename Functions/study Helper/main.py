from cards import showcards
from quiz import start_quiz

def main():
    while True:
        print("Welcome to Study Helper!")
        print("1. Learn some more new terms with flashcards")
        print("2. Test your knowldge with a quiz")
        print("3. Exit")


        choice = input("ENTER THE NUMBER OF YOUR CHOICE: ")


        if choice == '1':
            showcards()
        elif choice =='2':
            start_quiz()
        elif choice == '3':
            print("GOODBYE")
            break
        else:
            print("INVALID CHOICE, PLEASE TRY AGAIN")

if __name__=="__main__":
    main()