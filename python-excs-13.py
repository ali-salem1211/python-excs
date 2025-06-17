shopping_list = []

def show_menu():
    print("\n1. Add item")
    print("2. Show list")
    print("3. Remove item")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option: ")
    
    if choice == '1':
        item = input("Enter item to add: ")
        shopping_list.append(item)
    elif choice == '2':
        print("Current list:", shopping_list)
    elif choice == '3':
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            print("Item not found.")
    elif choice == '4':
        break
    else:
        print("Invalid choice.")
