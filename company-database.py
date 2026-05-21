# Company database
# Index:      0          1         2         3
names = ["alice", "bob", "charlie", "david"]
infos = ["Age: 21, Role: Admin", "Age: 25, Role: Developer", "Age: 19, Role: Design", "Age: 30, Role: Manager"]
infos_left = ["alice is the admin of the company, and controls access within the company","bob is the head developer, and internet operations manager of the company", "charlie is the main designer, and director of designs in the company", "david is the manager of the company and handles all managerial roles"]

print("--- User Search System ---")
search_name = input("Enter your name: ").lower()

found = False

for i in range(len(names)):
    if names[i] == search_name:
       
        print("\n--- Match Found! ---")
        print("Name:", names[i].capitalize())
        print("Info:", infos[i]) 
        
        found = True
       
        
        print("\nDo you want more info?")
        more_info = input("Yes(y) / No(n): ").lower()
        
       
        if more_info == 'yes' or more_info == 'y': 
            print("Here is more info on", names[i].capitalize())
            print(infos_left[i]) 
        else: 
            print("Thanks for Searching")
        
        break

if found == False:
    print(f"\nSorry, '{search_name}' was not found in our system.")
