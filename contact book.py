class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            for contact in self.contacts:
                print(contact)
                print("----------------------")
        else:
            print("No contacts found.")

    def search_contacts(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)

        if found_contacts:
            for contact in found_contacts:
                print(contact)
                print("----------------------")
        else:
            print("No matching contacts found.")

    def update_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)

        if found_contacts:
            print("Matching contacts found:")
            for index, contact in enumerate(found_contacts):
                print(f"{index + 1}. {contact}")

            choice = input("Enter the number of the contact to update: ")
            if choice.isdigit() and int(choice) in range(1, len(found_contacts) + 1):
                contact = found_contacts[int(choice) - 1]
                print("Enter new contact details:")
                name = input("Name: ")
                phone_number = input("Phone Number: ")
                email = input("Email: ")
                address = input("Address: ")

                contact.name = name
                contact.phone_number = phone_number
                contact.email = email
                contact.address = address

                print("Contact updated successfully.")
            else:
                print("Invalid choice.")

        else:
            print("No matching contacts found.")

    def delete_contact(self, search_term):
        found_contacts = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                found_contacts.append(contact)

        if found_contacts:
            print("Matching contacts found:")
            for index, contact in enumerate(found_contacts):
                print(f"{index + 1}. {contact}")

            choice = input("Enter the number of the contact to delete: ")
            if choice.isdigit() and int(choice) in range(1, len(found_contacts) + 1):
                contact = found_contacts[int(choice) - 1]
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
            else:
                print("Invalid choice.")

        else:
            print("No matching contacts found.")


# User Interface
def display_menu():
    print("Contact Management System")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Quit")


def get_menu_choice():
    return input("Enter your choice (1-6): ")


def get_contact_details():
    name = input("Name: ")
    phone_number = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    return name, phone_number, email, address


def main():
    contact_manager = ContactManager()

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == "1":
            name, phone_number, email, address = get_contact_details()
            contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(contact)

        elif choice == "2":
            contact_manager.view_contacts()

        elif choice == "3":
            search_term = input("Enter a name or phone number to search: ")
            contact_manager.search_contacts(search_term)

        elif choice == "4":
            search_term = input("Enter a name or phone number to search: ")
            contact_manager.update_contact(search_term)

        elif choice == "5":
            search_term = input("Enter a name or phone number to search: ")
            contact_manager.delete_contact(search_term)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a choice from 1-6.")


if __name__ == "__main__":
    main()
