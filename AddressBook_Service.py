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
        return (f" First name: {self.first_name}, Last Name: {self.last_name}, Address: {self.address}, City: {self.city}, Zip: {self.zip}, Phone-Number: {self.phone_number}, Email: {self.email} ")


# Addressbook Operations
class AddressBook:
    
    def __init__(self):
        self.contacts = {}

    # add contacts
    def add_contact(self):
        """
        Description : 
                This function passes the inputs from the user to conacts constructor and then appends the object of class contact to contacts list.
        Parameters : 
                self : for accessing default contacts list
        Returns :
                none
                prints contact added successfully
        """
        print("Please enter contact details to add contact")
        first_name =input("Enter first name: ")
        second_name = input("Enter second name: ")
        address =input("Enter address: ")
        city =input("Enter city: ")
        state =input("Enter state: ")
        zip =int(input("Enter zip: "))
        phone_number =int(input("Enter phone number: "))
        email_id = input("Enter email id: ")
        contact = Contact(first_name,second_name,address,city,state,zip,phone_number,email_id)
        self.contacts[first_name]= contact
        print("Contact Added Succesfully")


    def fetch_contact(self, first_name):
        """
        Description:
                This function fetches a contact from the contacts list using the first name.
        Parameters:
                first_name: First name of the contact to retrieve.
        Returns:
                contact: The contact from the contacts list.
        """
        for contact_key, contact_value in self.contacts.items():
            if contact_key == first_name:
                return contact_value
        return None
    
    # update address Book        
    def update_contact(self,first_name):
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
        contact = self.fetch_contact(first_name)
        if contact:
            print("Please enter contact details for update")
            first_name =input("Enter first name: ")
            second_name = input("Enter second name: ")
            address =input("Enter address: ")
            city =input("Enter city: ")
            state =input("Enter state: ")
            zip =int(input("Enter zip: "))
            phone_number =int(input("Enter phone number: "))
            email_id = input("Enter email id: ")
            new_contact = Contact(first_name,second_name,address,city,state,zip,phone_number,email_id)
            self.contacts[first_name] = new_contact
            print("Contact updated successfully")
        else:
            input("Contact not found. Hit enter to continue")


    # remove contact from address Book        
    def remove_contact(self,first_name):
        """
        Description :   
                    This function checks if the first name in present in contact 
                    if it is present, take the inputs from user again ,find the index number and update the contact. 
        Parameters :
                    self : self.contacts list.
        Returns :
                    none
                    prints update message.
        """
        contact = self.fetch_contact(first_name)
        if contact:
            del self.contacts[first_name]
            print("Contact removed successfully")
        else:
            input("Contact not found. Hit enter to continue")


    # display contacts from address Book
    def display_contact(self):
        """
        Description : 
                This function prints the object of class contact.
        Parameters :
                self : contacts dict containing multiple contacts 
        Returns:
                none
                prints key value from contact object
        """
        # iterate over contacts dict to print each contact
        print("|-------------------------------------------------------------------------------------------------|")
        for key ,values in self.contacts.items():
                print(f"{key} \n [{values}]")
                print()
        print("|-------------------------------------------------------------------------------------------------|")

        input("Contacts displayed, Hit Enter to continue!")




