#Company Database
users_database = {
    "alice": {
        "info": "Age: 21, Role: Admin",
        "more_info": "Alice is the admin of the company, and controls access within the company."
    },
    "bob": {
        "info": "Age: 25, Role: Developer",
        "more_info": "Bob is the head developer, and internet operations manager of the company."
    },
    "charlie": {
        "info": "Age: 19, Role: Design",
        "more_info": "Charlie is the main designer, and director of designs in the company."
    },
    "david": {
        "info": "Age: 30, Role: Manager",
        "more_info": "David is the manager of the company and handles all managerial roles."
    }
}

print("--- User Search System ---")
search_name = input("Enter your name: ").lower()


if search_name in users_database:
    print("\n--- Match Found! ---")
    print("Name:", search_name.capitalize())
    
    print("Info:", users_database[search_name]["info"])
    
    print("\nDo you want more info?")
    more_info = input("Yes(y) / No(n): ").lower()
    
    if more_info == 'yes' or more_info == 'y':
        print(f"Here is more info on {search_name.capitalize()}:")
        print(users_database[search_name]["more_info"])
    else:
        print("Thanks for Searching!")

else:
    print(f"\nSorry, '{search_name}' was not found in our system.")

