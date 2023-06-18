'''
@Author: shubham shirke
@Date: 2023-06-13 12:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2023-06-13 14:50:30
@Title : To add a contact in address book.
'''
from AddressBook_Service import *

def main():
    address_book = AddressBook()  # creating instace of a class
    while True:
        print()
        print("--Address Book System--")
        print("-----------------------")
        print("1.Add contact")
        print("2.Print Contact")
        print("3.Exit")
        print("-----------------------")
        choice = int(input("Enter choice: "))  
        if choice == 1:
            address_book.add_contact()

        elif choice == 2:
            address_book.display_contact()

        elif choice == 3:
            return False
        else:
            print("[error] Selected option is wrong")
            return main()
            
            

if __name__ == "__main__":
    main()
