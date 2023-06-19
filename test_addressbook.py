'''
@Author: shubham shirke
@Date: 2023-06-16 15:30:30
@Last Modified by: shubham shirke
@Last Modified time: 2022-06-17 18:16:30
@Title : Unit Test each function in address book system.
'''

import unittest

from AddressBook_Service import Contact , AddressBook

class TestAddressBook(unittest.TestCase):

    # predefined attributes
    def setUp(self) -> None:
        self.address_book = AddressBook()
        self.address_book_name = "home"
        self.first_name = "ramesh"
        self.contact = Contact("ramesh", "sawant", "Panvel", "kudal", "New York", "12345", "987654321","shirke@gmail.com")

    # Test case create address book
    def test_add_address_book(self):
        result_1 = self.address_book.add_address_books(self.address_book_name)    
        self.assertTrue(result_1)
        # Cheking for not accepting dublicate values
        result_2 = self.address_book.add_address_books(self.address_book_name)    
        self.assertFalse(result_2)

    # Test case fetch address book 
    def test_fetch_addressbook(self):
        self.address_book.add_address_books(self.address_book_name)
        result = self.address_book.fetch_address_book(self.address_book_name)
        if result != None:
            self.assertTrue(result)
        else:
            self.assertRaises(tuple)

    # Test case remove address book
    def test_remove_address_book(self):
        self.address_book.add_address_books(self.address_book_name)
        self.assertEqual(len(self.address_book.address_books),1)
        result = self.address_book.fetch_address_book(self.address_book_name)
        result1 = self.address_book.remove_address_book(result)
        self.assertTrue(result1)  
        self.assertEqual(len(self.address_book.address_books),0)   
    
    # Test case update address book , it checks only that name given by user exist in dictionary.
    def test_update_address_book(self):
        self.address_book.add_address_books(self.address_book_name)
        self.assertEqual(len(self.address_book.address_books),1)
        result = self.address_book.update_address_book("friend")
        self.assertFalse(result)

    # Test case display address book
    def test_display_address_book(self):
        self.address_book.add_address_books(self.address_book_name)
        self.assertEqual(len(self.address_book.address_books),1)
        result = self.address_book.display_address_books()
        self.assertTrue(result)

    # Test case to add contact:need to do manual entry of data. If not want to test this comment it.
    def test_add_contact(self):
        self.address_book.add_address_books(self.address_book_name)
        self.assertEqual(len(self.address_book.address_books),1)
        result = self.address_book.add_contact(self.address_book_name)
        self.assertTrue(result)

    # Test case to update contact:need to do manual entry of data. If not want to test this comment it.
    def test_update_contact(self):
        first_name = "ramesh"
        self.address_book.add_address_books(self.address_book_name)
        self.assertEqual(len(self.address_book.address_books),1)
        result = self.address_book.add_contact(self.address_book_name)
        if result == True:
            result = self.address_book.update_contact(self.address_book_name,first_name)
            self.assertTrue(result)
        
    # Test case to remove a contact
    def test_remove_contact(self):
        self.address_book.add_address_books(self.address_book_name)
        self.assertEqual(len(self.address_book.address_books),1)
        self.address_book.address_books[self.address_book_name][self.first_name] = self.contact
        result = self.address_book.remove_contact(self.address_book_name,self.first_name)
        self.assertTrue(result)
        
        # rajesh with contact should not be found
        result_1 = self.address_book.remove_contact(self.address_book_name,"rajesh") 
        self.assertFalse(result_1)

    # Test case to display all contacts
    def test_display_contact(self):
        self.address_book.add_address_books(self.address_book_name)
        self.assertEqual(len(self.address_book.address_books),1)
        self.address_book.address_books[self.address_book_name][self.first_name] = self.contact
        result = self.address_book.display_contacts(self.address_book_name)
        self.assertTrue(result)

    # Test case to search contact by state
    def test_search_by_state(self):
        self.address_book.add_address_books(self.address_book_name)
        self.assertEqual(len(self.address_book.address_books),1)
        self.address_book.address_books[self.address_book_name][self.first_name] = self.contact
        # check for option 1
        state_contacts,statename = self.address_book.search_address_book_by_state("New York",1)
        result = self.address_book.print_search_contacts(state_contacts,statename)
        self.assertTrue(result)
        #check for option 2
        state_contacts,statename = self.address_book.search_address_book_by_state("New York",2)
        result_1 = self.address_book.print_search_contacts(state_contacts,statename)
        self.assertTrue(result_1)
        # check for false state name
        state_contacts,statename = self.address_book.search_address_book_by_state("Kudal",2)
        result_1 = self.address_book.print_search_contacts(state_contacts,statename)
        self.assertFalse(result_1)

    # Test case to search contact by city
    def test_search_by_city(self):
        self.address_book.add_address_books(self.address_book_name)
        self.assertEqual(len(self.address_book.address_books),1)
        self.address_book.address_books[self.address_book_name][self.first_name] = self.contact
        # check for option 1
        city_contacts,cityname = self.address_book.search_address_book_by_city("kudal",1)
        result = self.address_book.print_search_contacts(city_contacts,cityname)
        self.assertTrue(result)
        # check for option 2
        city_contacts,cityname = self.address_book.search_address_book_by_city("kudal",2)
        result_1 = self.address_book.print_search_contacts(city_contacts,cityname)
        self.assertTrue(result_1)
        # check for false city name
        city_contacts,cityname = self.address_book.search_address_book_by_city("pandur",2)
        result_1 = self.address_book.print_search_contacts(city_contacts,cityname)
        self.assertFalse(result_1)

    # Test case to sort contact by city for option 1 and state for option 2
    def test_sort_addressbook(self):
        addressbook_name_1 = "friend"
        contact_1 = Contact("rajesh", "sawant", "Panvel", "mumbai", "maha", "12345", "987654321","shirke@gmail.com")
        contact_2 = Contact("sandip", "sawant", "Panvel", "surat", "maha", "12345", "987654321","shirke@gmail.com")
        self.address_book.add_address_books(self.address_book_name)
        self.assertEqual(len(self.address_book.address_books),1)
        self.address_book.address_books[self.address_book_name][self.first_name] = self.contact
        self.address_book.add_address_books(addressbook_name_1)
        self.address_book.address_books[addressbook_name_1][contact_1.first_name] = contact_1
        self.address_book.address_books[addressbook_name_1][contact_2.first_name] = contact_2
        # sort by city
        result_contacts = self.address_book.sort_address_book(1)
        result_1 = self.address_book.print_sorted_contacts(result_contacts)
        self.assertTrue(result_1)
        # sort by state
        result_contacts = self.address_book.sort_address_book(2)
        result_2 = self.address_book.print_sorted_contacts(result_contacts)
        self.assertTrue(result_2)
    
    # Test case for csv read
    def test_csv_read(self):
        result = self.address_book.read_address_books_from_csv("person1.csv")
        self.assertTrue(result)
        # check for file not found
        result_1 = self.address_book.read_address_books_from_csv("perso.csv")
        self.assertFalse(result_1)

    # Test case for csv Write
    def test_csv_write(self):
        self.address_book.add_address_books(self.address_book_name)
        self.address_book.address_books[self.address_book_name][self.first_name] = self.contact
        result = self.address_book.write_address_books_to_csv("person1.csv")
        self.assertTrue(result)
        
    # Test case for Json Read
    def test_json_read(self):
        result = self.address_book.read_address_books_from_json("person1.json")
        self.assertTrue(result)
        # check for file not found
        result_1 = self.address_book.read_address_books_from_json("perso.json")
        self.assertFalse(result_1)

    # Test case for Json Write
    def test_json_write(self):
        self.address_book.add_address_books(self.address_book_name)
        self.address_book.address_books[self.address_book_name][self.first_name] = self.contact
        result = self.address_book.write_address_books_to_json("person1.json")
        self.assertTrue(result)
        
    

if __name__ == "__main__":
    unittest.main()
