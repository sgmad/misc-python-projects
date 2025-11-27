from datetime import datetime

inventory = []
item_id = 1


def add_item():
    global item_id

    name = input("Enter item name: ")
    category = input("Enter item category (e.g., Snacks, Drinks, Supplies): ")
    price = input("Enter item price: ")
    stock = input("Enter item stock quantity: ")

    # Get the current date and time as a readable string
    date_added = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    item = {
        "ID": item_id,
        "Name": name,
        "Category": category,
        "Price": price,
        "Stock": stock,
        "DateAdded": date_added
    }

    inventory.append(item)
    item_id += 1

    print(f"\nItem '{name}' in category '{category}' added to the inventory.")


def remove_item():
    name = input("Enter the name of the item to remove: ")
    for item in inventory:
        if item["Name"].lower() == name.lower():
            inventory.remove(item)
            print(f"\nItem '{name}' has been removed from the inventory.")
            return
    print(f"\nItem '{name}' not found in the inventory.")


def search_items():
    mode = input("Search by 1=Category or 2=Name: ")

    if mode == "1":
        category = input("Enter category: ")
        found = [i for i in inventory if i["Category"].lower() == category.lower()]

        if not found:
            print(f"\nNo items found in category: {category}")
        else:
            print(f"\nItems in category '{category}':")
            for idx, i in enumerate(found, start=1):
                print(
                    f"{idx}. {i['Name']} | Price: {i['Price']} | Stock: {i['Stock']} "
                    f"| ID: {i['ID']} | Added: {i['DateAdded']}"
                )

    elif mode == "2":
        name = input("Enter item name (or part of it): ")
        found = [i for i in inventory if name.lower() in i["Name"].lower()]

        if not found:
            print(f"\nNo matching items found for: {name}")
        else:
            print("\nMatching items:")
            for idx, i in enumerate(found, start=1):
                print(
                    f"{idx}. {i['Name']} | Category: {i['Category']} | Price: {i['Price']} "
                    f"| Stock: {i['Stock']} | ID: {i['ID']} | Added: {i['DateAdded']}"
                )
    else:
        print("\nInvalid option.")


def display_all_items():
    if not inventory:
        print("\nNo items in the inventory.")
        return

    # Sort items alphabetically by name
    sorted_items = sorted(inventory, key=lambda i: i["Name"].lower())

    print("\nList of all items in the minimart:")
    for idx, i in enumerate(sorted_items, start=1):
        print(
            f"{idx}. {i['Name']} | Category: {i['Category']} | Price: {i['Price']} "
            f"| Stock: {i['Stock']} | ID: {i['ID']} | Added: {i['DateAdded']}"
        )


def main():
    global inventory, item_id

    while True:
        print("\n====== UNIVERSITY MINIMART MENU ======")
        print("1. Add an Item")
        print("2. Remove an Item")
        print("3. Search for an Item")
        print("4. Display All Items")
        print("5. Exit")

        option = input("Choose an option: ")

        if option == "1":
            add_item()
        elif option == "2":
            remove_item()
        elif option == "3":
            search_items()
        elif option == "4":
            display_all_items()
        elif option == "5":
            print("Thank you for using the University Minimart System!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
