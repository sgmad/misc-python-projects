from datetime import datetime

inventory = []
item_id = 1
data_file = "minimart_data.txt"


def load_data():
    global inventory, item_id

    try:
        with open(data_file, "r") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            parts = line.split(" | ")
            # Expected format:
            # ID | Name | Category | Price | Stock | DateAdded

            item = {
                "ID": int(parts[0]),
                "Name": parts[1],
                "Category": parts[2],
                "Price": parts[3],
                "Stock": parts[4],
                "DateAdded": parts[5]
            }

            inventory.append(item)

        if inventory:
            item_id = max(i["ID"] for i in inventory) + 1

    except FileNotFoundError:
        inventory = []
        item_id = 1


def save_data():
    with open(data_file, "w") as f:
        for item in inventory:
            line = (
                f"{item['ID']} | {item['Name']} | {item['Category']} | "
                f"{item['Price']} | {item['Stock']} | {item['DateAdded']}\n"
            )
            f.write(line)


def add_item():
    global item_id

    name = input("Enter item name: ")
    category = input("Enter item category (e.g., Snacks, Drinks, Supplies): ")
    price = input("Enter item price: ")
    stock = input("Enter item stock quantity: ")

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

    save_data()
    print(f"\nItem '{name}' added to the inventory.")


def remove_item():
    name = input("Enter the name of the item to remove: ")

    for item in inventory:
        if item["Name"].lower() == name.lower():
            inventory.remove(item)
            save_data()
            print(f"\nItem '{name}' has been removed.")
            return

    print(f"\nItem '{name}' not found.")


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

    sorted_items = sorted(inventory, key=lambda i: i["Name"].lower())

    print("\nList of all items:")
    for idx, i in enumerate(sorted_items, start=1):
        print(
            f"{idx}. {i['Name']} | Category: {i['Category']} | Price: {i['Price']} "
            f"| Stock: {i['Stock']} | ID: {i['ID']} | Added: {i['DateAdded']}"
        )


def main():
    load_data()

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
            print("Thank you for using the University Minimart System.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
