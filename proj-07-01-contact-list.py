from contact_class import Contact


print("Welcome to the Contact List App\n")

first_name = input("Enter first name: ")
last_name = input("Enter last name:  ")
email = input("Enter email:      ")
phone = input("Enter phone:      ")

contact = Contact(first_name, last_name, email, phone)
print(contact.display_contact())
print("bye")