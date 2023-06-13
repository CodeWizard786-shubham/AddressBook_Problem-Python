'''
@Author: shubham shirke
@Date: 2023-06-12 10:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2022-06-13 12:30:30
@Title : To add multiple address books in dictionary in address book system.
'''
from AddressBook_Service import *

def main():
    """
    Description : 
            This function is where the code execution starts. It provides user a interface to work with address book system.
    Parameters:
            none
    Returns : 
            none
            displays menu driven interface.
    """
    address_book = AddressBook()  # creating instance of a class

    while True:
        print()
        print("--AddressBook System--")
        print("----------------------")
        print("1.Add AddressBook")
        print("2.Remove AddressBook")
        print("3.Edit AddressBook")
        print("4.Print AddressBook")
        print("5.Exit")
        print("-------------------")
        user_choice = int(input("Enter choice: "))
        if user_choice == 1:
            address_book_name = input("Enter Address Book name: ")
            address_book.add_address_books(address_book_name)
        elif user_choice == 2:
            address_book_name = input("Enter Address Book name to remove: ")
            address_book.remove_address_book(address_book_name)
        elif user_choice == 3:
            address_book_name = input("Enter Address book name to update: ")
            address_book.update_address_book(address_book_name)
        elif user_choice == 4:
            address_book.display_address_books()
        elif user_choice == 4:
            print("Thank you for using Address Book system ")
            return False
        else :
            print("[error] : enter valid option")


if __name__ == "__main__":
    main()