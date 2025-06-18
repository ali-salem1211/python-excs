contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def search_contact(name):
    return contacts.get(name, "Contact not found.")

def display_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

# Example usage
add_contact("Alice", "123-456")
add_contact("Bob", "987-654")
print("Search for Alice:", search_contact("Alice"))
print("All contacts:")
display_contacts()
