print("--- My Contact Manager ---")

# Create an empty dictionary to hold the contacts
contacts = {}

while True:
    print("\n--- MENU ---")
    print("1. Add/Update Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")
    
    choice = input("\nChoose an option (1-5): ")
    
    # 1. ADD OR UPDATE A CONTACT
    if choice == "1":
        name = input("Enter contact name: ").lower()
        phone = input("Enter phone number: ")
       
        contacts[name] = phone
        print(f"Success! {name.capitalize()} has been saved.")
        
    # 2. SEARCH FOR A CONTACT
    elif choice == "2":
        search_name = input("Enter name to search: ").lower()
      
        if search_name in contacts:
            print(f"\nFound: {search_name.capitalize()} -> {contacts[search_name]}")
        else:
            print("\nContact not found.")
            
    # 3. DELETE A CONTACT
    elif choice == "3":
        delete_name = input("Enter name to delete: ").lower()
        
        if delete_name in contacts:
            contacts.pop(delete_name)
            print(f"{delete_name.capitalize()} successfully deleted.")
        else:
            print("\nThat contact doesn't exist.")
            
    # 4. VIEW ALL CONTACTS
    elif choice == "4":
        if len(contacts) == 0:
            print("\nYour contact book is empty!")
        else:
            print("\n--- All Contacts ---")
            
            for name, phone in contacts.items():
                print(f"- {name.capitalize()}: {phone}")
                
 # 5. EXIT THE APP
    elif choice == "5":
        print("\nClosing Contact Manager. Goodbye!")
        break
        
    else:
        print("\nInvalid choice! Please pick a number from 1 to 5.")
