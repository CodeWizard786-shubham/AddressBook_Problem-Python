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
        return (f" First name: {self.first_name}\n Last Name: {self.last_name}\n Address: {self.address}\n Name: {self.city}\n Zip: {self.zip}\n Phone-Number: {self.phone_number}\n Email: {self.email}")


# Addressbook Operations
class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact():
        """
        Description : 
                This function takes inputs from user, sents it to class contact through object and prints the contact result.
        Parameters : 
                none
        Returns :
                contact  - contact object __str__ function which overides the object.
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
        print("Contact Added Succesfully")

        return contact
        
        
    def display_contact(contact):
        """
        Description : 
                This function prints the object of class contact.
        Parameters :
                contact : return object from add_contact function.
        Returns:
                none
                prints contact object
        """
        print(contact)




