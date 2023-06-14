'''
@Author: shubham shirke
@Date: 2023-06-12 10:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2022-06-14 21:30:30
@Title : Sorting contacts uising first name from address book to print in alphabetical order..
'''
from logger import logger
from AddressBook_Service import *


def main():
    logger.info('Starting the program')
    """
    Description : 
            This function is where the code execution starts. It provides user a interface to work with address book system.
    Parameters:
            none
    Returns : 
            none
            displays menu driven interface.
    """
    try:
        address_book = AddressBook()  # creating instance of a class

        while True:
            print()
            print("--AddressBook System--")
            print("----------------------")
            print("1.Add AddressBook")
            print("2.Remove AddressBook")
            print("3.Edit AddressBook")
            print("4.Search AddressBook")
            print("5.Print AddressBook")
            print("6.Exit")
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
                while True:
                    print()
                    print("--Search contacts in AddressBook--")
                    print("1. Search by state")
                    print("2. Search by City")
                    print("3. Exit")
                    user_search_choice =int(input("Enter choice: "))
                    #search by state
                    if user_search_choice == 1: 
                        state_name = input("Enter state name to search: ")
                        print("Enter choice: \n 1:Display contact names \n 2:Display full contacts")
                        user_state_choice = int(input("Enter choice: "))
                        if user_state_choice == 1:
                            state_contacts,state_name = address_book.search_address_book_by_state(state_name,user_state_choice)
                            address_book.print_search_contacts(state_contacts,state_name)
                        elif user_state_choice == 2:
                            state_contacts,search_name = address_book.search_address_book_by_state(state_name,user_state_choice)
                            address_book.print_search_contacts(state_contacts,state_name)
                        elif user_state_choice == 3:
                            break
                        else:
                            logger.warning("Invalid option: enter correct option")
                    # search by city
                    elif user_search_choice == 2: 
                        city_name = input("Enter city name to search: ")
                        print("Enter choice: \n 1:Display contact names \n 2:Display full contacts")
                        user_city_choice = int(input("Enter choice: "))
                        if user_city_choice == 1:
                            city_contacts,city_name = address_book.search_address_book_by_city(city_name,user_city_choice)
                            address_book.print_search_contacts(city_contacts,city_name)
                        elif user_city_choice == 2:
                            city_contacts,city_name = address_book.search_address_book_by_city(city_name,user_city_choice)
                            address_book.print_search_contacts(city_contacts,city_name)
                        elif user_state_choice == 3:
                            break
                        else:
                            logger.warning("Invalid option: enter correct option")
                    elif user_search_choice == 3:
                        break
                    else:
                        logger.warning("Please enter correct choice")
            elif user_choice == 5:
                address_book.display_address_books()
            elif user_choice == 6:
                logger.info("Thank you for using Address Book system ")
                return False
            else :
                logger.error("[error] : enter valid option")
    except Exception as e:
         logger.error('An error occurred: %s', str(e))

    logger.info('Program finished')


if __name__ == "__main__":
    main()
