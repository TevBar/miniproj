import re
import os

# Initialize the contact storage
contacts = {}

# Helper function to validate inputs
def validate_input(pattern, input_str, field_name):
    if not re.match(pattern, input_str):
        raise ValueError(f"Invalid {field_name}.")
    return input_str

# Function to display the menu
def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file *BONUS*")
    print("8. Quit")

# Function to add a new contact
def add_contact():
    try:
        unique_id = input("Enter unique identifier (email or phone): ")
        validate_input(r"^[\w\.-]+@[\w\.-]+\.\w+$|^\d{10}$", unique_id, "identifier (email or phone)")

        if unique_id in contacts:
            print("Contact already exists.")
            return

        name = input("Enter name: ")
        phone = validate_input(r"^\d{10}$", input("Enter phone number (10 digits): "), "phone number")
        email = validate_input(r"^[\w\.-]+@[\w\.-]+\.\w+$", input("Enter email address: "), "email")
        address = input("Enter address: ")
        notes = input("Enter additional notes: ")

        contacts[unique_id] = {"Name": name, "Phone": phone, "Email": email, "Address": address, "Notes": notes}
        print("Contact added successfully.")
    except ValueError as e:
        print(e)

# Function to edit a contact
def edit_contact():
    unique_id = input("Enter the unique identifier of the contact to edit: ")
    if unique_id not in contacts:
        print("Contact not found.")
        return

    contact = contacts[unique_id]
    print(f"Editing contact: {contact}")
    try:
        contact["Name"] = input(f"Enter new name (current: {contact['Name']}): ") or contact["Name"]
        contact["Phone"] = validate_input(r"^\d{10}$", input(f"Enter new phone (current: {contact['Phone']}): ") or contact["Phone"], "phone number")
        contact["Email"] = validate_input(r"^[\w\.-]+@[\w\.-]+\.\w+$", input(f"Enter new email (current: {contact['Email']}): ") or contact["Email"], "email")
        contact["Address"] = input(f"Enter new address (current: {contact['Address']}): ") or contact["Address"]
        contact["Notes"] = input(f"Enter new notes (current: {contact['Notes']}): ") or contact["Notes"]
        print("Contact updated successfully.")
    except ValueError as e:
        print(e)

# Function to delete a contact
def delete_contact():
    unique_id = input("Enter the unique identifier of the contact to delete: ")
    if unique_id in contacts:
        del contacts[unique_id]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

# Function to search for a contact
def search_contact():
    unique_id = input("Enter the unique identifier of the contact to search for: ")
    if unique_id in contacts:
        print("Contact details:", contacts[unique_id])
    else:
        print("Contact not found.")

# Function to display all contacts
def display_all_contacts():
    if not contacts:
        print("No contacts available.")
        return
    for unique_id, details in contacts.items():
        print(f"{unique_id}: {details}")

# Function to export contacts to a file
def export_contacts():
    filename = input("Enter filename to export contacts (e.g., contacts.txt): ")
    try:
        with open(filename, "w") as file:
            for unique_id, details in contacts.items():
                file.write(f"{unique_id}: {details}\n")
        print(f"Contacts exported successfully to {filename}.")
    except Exception as e:
        print(f"Error exporting contacts: {e}")

# Function to import contacts from a file
def import_contacts():
    filename = input("Enter filename to import contacts from: ")
    try:
        if not os.path.exists(filename):
            print("File not found.")
            return
        with open(filename, "r") as file:
            for line in file:
                unique_id, details = line.strip().split(":", 1)
                details = eval(details.strip())  # Convert string back to dictionary
                contacts[unique_id] = details
        print("Contacts imported successfully.")
    except Exception as e:
        print(f"Error importing contacts: {e}")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            edit_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_all_contacts()
        elif choice == "6":
            export_contacts()
        elif choice == "7":
            import_contacts()
        elif choice == "8":
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
