Contact Management System
The Contact Management System is a command-line application that allows users to efficiently manage their contacts. This system provides various features, including adding, editing, deleting, searching, and displaying contacts. It also supports exporting and importing contact data to and from text files.

Features
Add a New Contact

Add new contacts with details like name, phone number, email, address, and notes.
Unique identifier: Either a valid email address or a phone number.
Edit an Existing Contact

Modify contact details such as name, phone number, email, etc.
Delete a Contact

Remove a contact from the system using its unique identifier.
Search for a Contact

Retrieve details of a specific contact using the unique identifier.
Display All Contacts

View a list of all stored contacts with their details.
Export Contacts to a Text File

Save all contacts to a text file in a structured format.
Import Contacts from a Text File (Bonus Feature)

Load contacts from a text file into the system.
Quit

Exit the application gracefully.
Technologies Used
Language: Python
Data Structure: Nested dictionaries for contact storage
Input Validation: Regular expressions (regex)
File Handling: Reading and writing text files
Installation and Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/TevBar/ContactManagementSystem.git
cd ContactManagementSystem
Run the Program: Make sure you have Python installed. Execute the program:

bash
Copy code
python contact_management_system.py
How to Use
When the program starts, you'll see a menu with options.
Select a menu option by entering the corresponding number (e.g., 1 to add a contact).
Follow the prompts to perform the desired action.
To quit the application, enter 8 from the main menu.
Input Validation
Email Address: Must follow the standard format (e.g., example@example.com).
Phone Number: Must be exactly 10 digits.
Errors during validation will prompt the user to re-enter the correct format.
File Export and Import
Export Contacts:

Select Option 6 and provide a filename (e.g., contacts.txt).
The program saves all contact data to the specified file.
Import Contacts (Bonus):

Select Option 7 and provide the filename (e.g., contacts.txt).
Contacts in the file will be added to the system.
Error Handling
The system uses try-except blocks to handle:
Invalid input formats
File read/write errors
Missing contacts or duplicate identifiers
Example Output
mathematica
Copy code
Welcome to the Contact Management System!
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Import contacts from a text file *BONUS*
8. Quit

Enter your choice (1-8): 1
Enter unique identifier (email or phone): john.doe@example.com
Enter name: John Doe
Enter phone number (10 digits): 1234567890
Enter address: 123 Maple Street
Enter additional notes: Best friend
Contact added successfully.
Contributing
Feel free to fork this repository and submit pull requests for new features or bug fixes. All contributions are welcome!
