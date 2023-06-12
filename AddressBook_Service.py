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
        return (f" First name: {self.first_name}\n Last Name: {self.last_name}\n Address: {self.address}\n Name: {self.city}\n Zip: {self.zip}\n Phone-Number: {self.phone_number}\n Email: {self.email}\n")


# Addressbook Operations
class AddressBook:
    
    def __init__(self):
        self.contacts = []

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
        first_name =input("Enter first name: ")
        second_name = input("Enter second name: ")
        address =input("Enter address: ")
        city =input("Enter city: ")
        state =input("Enter state: ")
        zip =int(input("Enter zip: "))
        phone_number =int(input("Enter phone number: "))
        email_id = input("Enter email id: ")
        contact = Contact(first_name,second_name,address,city,state,zip,phone_number,email_id)
        self.contacts.append(contact)
        print("Contact Added Succesfully")


    def fetch_contact(self,first_name):
        for contact in self.contacts:
            if contact.first_name == first_name:
                return contact
        return None
    
    # update address Book        
    def update_contact(self,first_name):
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
            first_name =input("Enter first name: ")
            second_name = input("Enter second name: ")
            address =input("Enter address: ")
            city =input("Enter city: ")
            state =input("Enter state: ")
            zip =int(input("Enter zip: "))
            phone_number =int(input("Enter phone number: "))
            email_id = input("Enter email id: ")
            new_contact = Contact(first_name,second_name,address,city,state,zip,phone_number,email_id)
            index = self.contacts.index(contact)
            self.contacts[index] = new_contact
            print("Contact updated successfully")
        else:
            input("Contact not found. Hit enter to continue")

    # display address Book
    def display_contact(self):
        """
        Description : 
                This function prints the object of class contact.
        Parameters :
                contact : return object from add_contact function.
        Returns:
                none
                prints contact object
        """
        # iterate over contacts list to print each contact
        for contact in self.contacts:
            if contact in self.contacts:
                print(contact)
            else:
                print("Contact not found")
        input("Contacts displayed, Hit Enter to continue!")




