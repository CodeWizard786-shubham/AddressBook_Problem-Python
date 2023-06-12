from AddressBook_Service import AddressBook

def main():
    
    while True:
        print("--Address Book System--")
        print("-----------------------")
        print("1.Add contact")
        print("2.Print Contact")
        print("3.Exit")
        choice = int(input("Enter choice: "))  
        if choice == 1:
            contact = AddressBook.add_contact()

        elif choice == 2:
            AddressBook.display_contact(contact)

        elif choice == 3:
            return False
            
            

if __name__ == "__main__":
    main()