"""
This is the original template file that will remain unchanged.
"""

class Email:
    """Email class to represent an email object"""
    
    def __init__(self, email_address, subject_line, email_content):
        """Constructor to initialize an email object"""
        # TODO: Initialize instance variables
        pass
    
    def mark_as_read(self):
        """Method to mark an email as read"""
        # TODO: Implement this method
        pass


# Empty list to store email objects
inbox = []


def populate_inbox():
    """Function to populate inbox with sample emails"""
    # TODO: Create and add sample email objects to inbox
    pass


def list_emails():
    """Function to list all emails with their indices"""
    # TODO: Display all emails with their subject lines
    pass


def read_email(index):
    """Function to read a specific email"""
    # TODO: Display the selected email and mark it as read
    pass


# Main program
def main():
    """Main program loop"""
    populate_inbox()
    
    while True:
        print("\n" + "="*50)
        print("EMAIL SIMULATOR")
        print("="*50)
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")
        print("-"*50)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == "1":
            # TODO: Implement read email functionality
            pass
            
        elif choice == "2":
            # TODO: Implement view unread emails functionality
            pass
            
        elif choice == "3":
            print("\nThank you for using Email Simulator. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()