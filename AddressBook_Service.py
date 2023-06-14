from logger import logger
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
            else:
                self.address_books[address_book_name] = {}
                logger.info(f"Address Book with name '{address_book_name}' is successfully created")
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
        else:
            logger.warning(f"Address Book with name {address_book_name} not found")

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
            else:
                logger.warning(f"Contacts from '{search_name}' not found")
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
            else:
                logger.warning(f"Contact with name '{first_name}' already exists")
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
            else:
                logger.warning("Contact not found")
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
            else:
                logger.warning("Contact not found")
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
            else:
                logger.warning(f"contacts not found in '{address_book_name}'")

            logger.info("Contacts displayed")
        except Exception as e:
            logger.error('An error occurred: %s', str(e))






