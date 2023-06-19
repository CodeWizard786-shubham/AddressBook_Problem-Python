from logger import logger
import os
import ast
import csv
import json
# class Contact with user inputs
class Contact:
    def __init__(self, first_name,last_name,address,city,state,zip,phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
        self.email = email
    
    def __str__(self):
        return (f" First name: {self.first_name}, Last Name: {self.last_name}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zip}, Phone-Number: {self.phone_number}, Email: {self.email} ")


# Addressbook Operations
class AddressBook:
    
    def __init__(self):
        """
        Description : 
                Default constructor.
        Resturns : address books dictionary
        """
        self.address_books = {}

    # read from file
    def read_address_books_from_file(self, filename):
        """
        Description : 
                    This function fetches contents from a text file and stores it in the address_books dictionary.
                    Here the contact object is serialize(str to contact object)   
        Parameters :
                    filename : name of the file to read from
        Returns    : 
                    none            
        """
        try:
            with open(filename, 'r') as file:
                data = ast.literal_eval(file.read())
                self.address_books = {}
                self.address_books = {address_book_name: {contact_name: Contact(**contact_data)
                                                          for contact_name, contact_data in address_book.items()}
                                      for address_book_name, address_book in data.items()}
            logger.info(f"Address books loaded from '{filename}'")
        except FileNotFoundError:
            with open(filename, 'w') as file:
                file.write(f"{{}}")
                print(f"File '{filename}' created.")
        except Exception as e:
            logger.error(f"An error occurred while reading address books from file: {str(e)}")
    
    # write to file
    def write_address_books_to_file(self, filename):
        """
        Description : 
                    This function stores contents to a text file from the address_books dictionary in a format.
                    Here the contact object is deserialize(contact object to str)   
        Parameters :
                    filename : name of the file to write
        Returns    : 
                    none            
        """
        try:
            data = {address_book_name: {contact_name: contact.__dict__
                                        for contact_name, contact in address_book.items()}
                    for address_book_name, address_book in self.address_books.items()}
            with open(filename, 'w') as file:
                file.write(str(data))
            logger.info(f"Address books saved to '{filename}'")
        except Exception as e:
            logger.error(f"An error occurred while writing address books to file: {str(e)}")

    # read csv file
    def read_address_books_from_csv(self, filename):
        """
        Description: 
            This function reads the address books from a CSV file and populates the address_books dictionary.
        Parameters:
            filename: Name of the CSV file to read.
        Returns:
            None
        """
        try:
            self.address_books = {}  # Clear existing address books

            with open(filename, 'r', newline='') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    address_book_name = row['AddressBook Name']
                    contact_name = row['Contact Name']
                    contact = Contact(
                        row['First name'],
                        row['Last Name'],
                        row['Address'],
                        row['City'],
                        row['State'],
                        row['Zip Code'],
                        row['Phone Number'],
                        row['Email ID']
                    )

                    if address_book_name not in self.address_books:
                        self.address_books[address_book_name] = {}

                    self.address_books[address_book_name][contact_name] = contact

            logger.info(f"Address books loaded from '{filename}'")
            return True
        except FileNotFoundError:
            logger.warning(f"File '{filename}' not found. Creating a new address book.")
            self.address_books = {}
            return False
        except Exception as e:
            logger.error(f"An error occurred while reading address books from file: {str(e)}")
       

    # write csv file
    def write_address_books_to_csv(self,filename):
        """
        Description: 
                This function stores contents to a CSV file from the address_books dictionary.
        Parameters:
                filename: name of the CSV file to write
        Returns: 
                None            
        """
        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['AddressBook Name', 'Contact Name', 'First name','Last Name','Address','City','State','Zip Code','Phone Number','Email ID'])
                for address_book_name, address_book in self.address_books.items():
                    for contact_name, contact in address_book.items():
                        writer.writerow([address_book_name, contact_name, contact.first_name,contact.last_name,contact.address,contact.city,contact.state,contact.zip,contact.phone_number,contact.email])
            logger.info(f"Address books saved to '{filename}'")
            return True
        except Exception as e:
            logger.error(f"An error occurred while writing address books to file: {str(e)}")
            return False

    # read Json file
    def read_address_books_from_json(self,filename):
        """
        Description: 
                This function fetches content from json file and stores to the address_books dictionary.
        Parameters:
                filename: name of the json file to write
        Returns: 
                None            
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.address_books = {address_book_name: {contact_name: Contact(**contact_data)
                                                          for contact_name, contact_data in address_book.items()}
                                      for address_book_name, address_book in data.items()}
            logger.info(f"Address books loaded from '{filename}'")
            return True
        except FileNotFoundError:
            logger.warning(f"File '{filename}' not found.Creating a new address book.")
            return False
        except Exception as e:
            logger.error(f"An error occurred while reading address books from file: {str(e)}")

    # write Json file
    def write_address_books_to_json(self,filename):
        """
        Description: 
                This function stores contents to a json file from the address_books dictionary.
        Parameters:
                filename: name of the json file to write
        Returns: 
                None            
        """
        try:
            data = {address_book_name: {contact_name: contact.__dict__
                                        for contact_name, contact in address_book.items()}
                    for address_book_name, address_book in self.address_books.items()}
            with open(filename, 'w') as file:
                json.dump(data, file, indent=4)
            logger.info(f"Address books saved to '{filename}'")
            return True
        except Exception as e:
            logger.error(f"An error occurred while writing address books to file: {str(e)}")
            return False


    def add_address_books(self,address_book_name):
        """
        Description : 
                This function creates a address book if it is already not present.
        Parameters :
                address_boo_name : address book name input from the user.
        Returns :
                none
                prints message
        """
        try:
            if address_book_name in self.address_books:
                logger.warning(f"Address Book with name '{address_book_name}' already exists.")  
                return False
            else:
                self.address_books[address_book_name] = {}
                logger.info(f"Address Book with name '{address_book_name}' is successfully created")
                return True
        except Exception as e:
            logger.error('An error occurred: %s', str(e))


    def fetch_address_book(self,address_book_name):
        """
        Description : 
                    This function feches address books from the address books dictionary.
        Parameters :
                    address_bbok_name : name of the address book to fetch.
        Returns :
                    address_book_value : contacts from address book
        """
        for address_book_key, address_book_value in self.address_books.items():
            if address_book_key == address_book_name:
                return address_book_key
        return None        


    def remove_address_book(self,address_book_name):
        """
        Description : 
                This function takes address book name from user and if it exist in address books dictionary deletes the particular address book.
        Parameters  :
                address_book_name : name of the address book to delete.
        Retruns :
                none
                print delete message
        """
        address_book = self.fetch_address_book(address_book_name)

        if address_book:
            self.address_books.pop(address_book_name)
            logger.info("Removed Address Book successfully")
            return True
        else:
            logger.warning(f"Address Book with name {address_book_name} not found")
            return False

    # edit address_book
    def update_address_book(self,address_book_name):
        """
        Description : 
                    This function allows to edit particular address book. Managing contacts from address book.
        Parameters :
                    address_book_name : name of the address book to edit.
        Returns    :
                    logs
                    displays contact system interface
        """
        if address_book_name not in self.address_books:
            logger.warning(f"Address Book with name '{address_book_name}' does not exists.")   
            return False  
        else:
            while True:
                print()
                print("--Contacts--")
                print("-----------------------")
                print("1.Add contact")
                print("2.Update Contact")
                print("3.Remove contact")
                print("4.Print Contact")
                print("5.Exit")
                print("-----------------------")
                choice = int(input("Enter choice: "))  
                if choice == 1:
                    self.add_contact(address_book_name)

                elif choice == 2:
                    first_name = input("Enter first name to update: ")
                    self.update_contact(address_book_name,first_name)

                elif choice == 3:
                    first_name = input("Enter first name to remove: ")
                    self.remove_contact(address_book_name,first_name)

                elif choice == 4:
                    self.display_contacts(address_book_name)

                elif choice == 5:
                    return False
                else:
                    logger.error("[error] Selected option is wrong")

    # display address Book
    def display_address_books(self):
        """
        Description : 
                This function prints the contents from the address_books dictionary.
        Parameters :
                self : address_books dictionary which is declared in default constructor.
        Returns :
                none
                prints address book name , contact from address book
        """
        try:
            if len(self.address_books) >=1 :
                for address_book_name, address_book in self.address_books.items():
                    print()
                    print(f"| AddressBook:{address_book_name} |")
                    print("|------------------------------------------------------------------------------------------------------------------------------|")
                    contact_number = 1
                    sorted_contacts = sorted(address_book.items(), key=lambda contact: contact[0])
                    for contact_name, contact in sorted_contacts:
                        print(f"| Contact {contact_number}: {contact_name} : {contact}|")
                        contact_number += 1
                    logger.info("Address Book Records displayed Succesfully")
                return True
            else:
                logger.warning("Address books not found")
                return False
        except Exception as e:
            logger.error('An error occurred: %s', str(e))

    # search contacts by state    
    def search_address_book_by_state(self, state_name,user_state_choice):
        """
        Description : 
                This function searches all the address books to find contacts with user specified state_name. 
        Parameters :
                self : self.address_books is the main address book system dictionary
                state_name : name of the state by user input to find contacts
                user_state_choice : choice option to find name or whole contacts for state. 
        Returns   :
                state_contacts : state contacts dictionary
        """

        try:
            state_contacts = {}
            if user_state_choice == 1:
                for address_book_name, address_book in self.address_books.items():
                    for contact_name, contact in address_book.items():
                        if contact.state == state_name:
                            state_contacts[contact_name] = contact.state
                return state_contacts,state_name
            elif user_state_choice == 2:
                for address_book_name, address_book in self.address_books.items():
                    for contact_name, contact in address_book.items():
                        if contact.state == state_name:
                            state_contacts[contact_name] = contact
                return state_contacts,state_name
        except Exception as e:
            logger.warning(f" contacts with '{state_name}' not found")

    # search contacts by city.    
    def search_address_book_by_city(self, city_name,user_city_choice):
        """
        Description : 
                This function searches all the address books to find contacts with user specified city_name.
        Parameters :
                self : self.address_books is the main address book system dictionary
                city_name : name of the state or city by user input to find contacts
                user_city_choice : choice option to find name or whole contacts for city. 
        Returns   :
                city_contacts : state or city contacts dictionary
        """

        try:
            city_contacts = {}
            if user_city_choice == 1:
                for address_book_name, address_book in self.address_books.items():
                    for contact_name, contact in address_book.items():
                        if contact.city == city_name:
                            city_contacts[contact_name] = contact.city
                return city_contacts,city_name
            elif user_city_choice == 2:
                for address_book_name, address_book in self.address_books.items():
                    for contact_name, contact in address_book.items():
                        if contact.city == city_name:
                            city_contacts[contact_name] = contact
                return city_contacts,city_name
        except Exception as e:
            logger.warning(f" contacts with '{city_name}' not found")

    # print contats from state_contacts dictionary
    def print_search_contacts(self,search_contacts,search_name):
        """
        Description : 
                This function prints each contact from search_contacts dict.
        Parameters :
                search_contacts : dictionary of state or city contacts.
        Returns :
                none
                prints contacts 
        """
        try:
            search_count_count = len(search_contacts) 
            if len(search_contacts) >= 1:
                print(f"contacts count by '{search_name}': {search_count_count}")
                print(f"The contacts are:")
                for search_name,contact in search_contacts.items():           
                    print(f"Name:'{search_name}' \n[{contact}]")

                return True
            else:
                logger.warning(f"Contacts from '{search_name}' not found")
                return False
        except Exception as e:
            logger.error('An error occurred: %s', str(e))

    # sort address_book
    def sort_address_book(self, user_sort_choice):
        """
        Description : 
                This function stores the contacs from the address books to sorted contacts dictionary . key as city or state and value as contact.
        Parameters :
                user_sort_choice : user choice option to get contacts for state or city.
        Returns :
                sorted_contacts : dictionary consisting state or city as key and contacts as value.
        """
        try:
            sorted_contacts = {}
            if user_sort_choice == 1:
                for address_book_name, address_book in self.address_books.items():
                    for contact_name, contact in address_book.items():
                        if contact.city not in sorted_contacts:
                            sorted_contacts[contact.city] = contact

            elif user_sort_choice == 2:
                for address_book_name, address_book in self.address_books.items():
                    for contact_name, contact in address_book.items():
                        if contact.state not in sorted_contacts:
                            sorted_contacts[contact.state] = contact
            return sorted_contacts

        except Exception as e:
            logger.warning("Contact not found")

    # print sorted address book
    def print_sorted_contacts(self, sorted_contacts):
        try:
            if len(sorted_contacts) >= 1:
                sorted_contacts = dict(sorted(sorted_contacts.items()))
                print()
                for sort_name, contact in sorted_contacts.items():
                    print(f"{sort_name}: {contact}")
                print()
                return True
            else:
                logger.warning("Contacts not found")
                return False

        except Exception as e:
            logger.error('An error occurred: %s', str(e))

    # add contacts
    def add_contact(self,address_book_name):
        """
        Description : 
                This function passes the inputs from the user to conacts constructor and then appends the object of class contact to contacts list.
        Parameters : 
                self : for accessing default contacts list
        Returns :
                none
                prints contact added successfully
        """
        try:
            print("Please enter contact details to add contact")
            first_name =input("Enter first name: ")
            contact = self.fetch_contact(address_book_name,first_name)
            if not contact:
                second_name = input("Enter second name: ")
                address =input("Enter address: ")
                city =input("Enter city: ")
                state =input("Enter state: ")
                zip =int(input("Enter zip: "))
                phone_number =int(input("Enter phone number: "))
                email_id = input("Enter email id: ")
                contact = Contact(first_name,second_name,address,city,state,zip,phone_number,email_id)
                self.address_books[address_book_name][first_name] = contact
                logger.info("Contact Added Succesfully")
                return True
            else:
                logger.warning(f"Contact with name '{first_name}' already exists")
                return False
        except Exception as e:
            logger.error('An error occurred: %s', str(e))

    # search contact in address book
    def fetch_contact(self, address_book_name, first_name):
        """
        Descrption : 
                    This function searches a contact from address book it it exist or not.
        Parameters :
                    self : default constructor
                    address_book_name : name of the address_book for fetching
                    first_name : first name from the address  book to fetch. 
        
        """
        address_book = self.address_books.get(address_book_name)
        if address_book:
            return address_book.get(first_name)
        return None
    
    # update address Book        
    def update_contact(self,address_book_name,first_name):
        """
        Description :   
                    This function checks if the first name in present in contact 
                    if it is present, take the inputs from user again ,update the contact as per key from contacts dictionary. 
        Parameters :
                    self : self.contacts list.
        Returns :
                    none
                    prints update message.
        """
        try:
            contact = self.fetch_contact(address_book_name,first_name)
            if contact:
                print("Please enter contact details for update")
                new_first_name =input("Enter first name: ")
                second_name = input("Enter second name: ")
                address =input("Enter address: ")
                city =input("Enter city: ")
                state =input("Enter state: ")
                zip =int(input("Enter zip: "))
                phone_number =int(input("Enter phone number: "))
                email_id = input("Enter email id: ")
                new_contact = Contact(new_first_name,second_name,address,city,state,zip,phone_number,email_id)
                self.address_books[address_book_name][new_first_name] = new_contact

            if first_name != new_first_name:
                del self.address_books[address_book_name][first_name]

                logger.info("Contact updated successfully")
                return True
            else:
                logger.warning("Contact not found")
                return False
        except Exception as e:
            logger.error('An error occurred: %s', str(e))



    # remove contact from address Book        
    def remove_contact(self,address_book_name,first_name):
        """
        Description :   
                    This function checks if the first name in present in contact 
                    if it is present, take the inputs from user again ,find the index number and update the contact. 
        Parameters :
                    self : self.addressbooks.
                    address_book_name : get name of addressbook
                    first_name : first name of the contact to remove.
        Returns :
                    none
                    prints update message.
        """
        try:
            contact = self.fetch_contact(address_book_name,first_name)
            if contact:
                del self.address_books[address_book_name][first_name]
                logger.info("Contact removed successfully")
                return True
            else:
                logger.warning("Contact not found")
                return False
        except Exception as e:
            logger.error('An error occurred: %s', str(e))

    # display contacts from address Book
    def display_contacts(self, address_book_name):
        try:
            address_book = self.address_books.get(address_book_name)
            if address_book:
                contact_number = 1
                sorted_contacts = sorted(address_book.items(), key=lambda contact: contact[0])
                print("|-----------------------------------------------------------------|")
                print(f"|  Contacts in '{address_book_name}'                             |")                           
                print("|-----------------------------------------------------------------|")
                for contact_name,contact in sorted_contacts:
                    print(f"Contact {contact_number}: {contact}")
                    print()
                    contact_number +=1
                print("|-----------------------------------------------------------------|")
                logger.info("Contacts Displayed successfully")
                return True
            else:
                logger.warning(f"contacts not found in '{address_book_name}'")
                return False
        except Exception as e:
            logger.error('An error occurred: %s', str(e))







