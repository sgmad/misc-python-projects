# code 837885

from datetime import datetime
import random
import sys

inventory = []
transactions = []



def display_inventory():
    
    if not inventory:
        print("\nInventory is empty.")
        return inventory

    print(f"\n{'CODE':<6} {'NAME':<20} {'PRICE':>8} {'STOCK':>8}")
    for p in inventory:
        print(f"{p['code']:<6} {p['name']:<20} {p['price']:>8.2f} {p['stock']:>8}")
    return inventory




def add_product(code, name, price, stock=0):

    code = str(code).upper()
    if any(p['code'].upper() == code for p in inventory):
        raise ValueError(f"Product with code {code} already exists.")

    if price < 0 or stock < 0:
        raise ValueError("Price and stock must not be negative")

    product = {"code": code, "name": str(name), "price": float(price), "stock": int(stock)}
    inventory.append(product)

    return product




def update_stock(code, quantity):

    item = next((p for p in inventory if p['code'].upper() == str(code).upper()), None)

    if item is None:
        raise LookupError(f"Product code {code} not found")

    if not isinstance(quantity, int):
        raise TypeError("Quantity must be an integer (positive or negative)")

    new_stock = item['stock'] + quantity
    if new_stock < 0:
        raise ValueError("Resulting stock cannot be negative")

    item['stock'] = new_stock
    return item




def purchase_product(code, quantity):

    item = next((p for p in inventory if p['code'].upper() == str(code).upper()), None)
    if item is None:
        raise LookupError(f"Product code {code} not found")

    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    product = item
    if product['stock'] < quantity:
        raise ValueError("Not enough stock available")

    # deduct stock if you buy
    product['stock'] -= quantity

    total = round(product['price'] * quantity, 2)

    # create receipt
    transaction = {
        'receipt': f"R{random.randint(0000000, 9999999)}", # unique receipt number
        'code': product['code'],
        'name': product['name'],
        'quantity': quantity,
        'unit_price': product['price'],
        'total': total,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    transactions.append(transaction)

    # print receipt
    print('\n' + '=' * 30)
    print(' UM MiniMart Receipt '.center(30, '='))
    print('=' * 30)
    print(f"Receipt: {transaction['receipt']}")
    print(f"Date:    {transaction['date']}")
    print('-' * 30)
    print(f"{transaction['name']} x{transaction['quantity']} @ {transaction['unit_price']:.2f}")
    print(f"Total: PHP {transaction['total']:.2f}")
    print('=' * 30 + '\n')

    return transaction




def delete_product(code):

    for i, p in enumerate(inventory):
        if p['code'].upper() == str(code).upper():
            return inventory.pop(i)
        
    raise LookupError(f"Product code {code} not found")




def search_products(keyword):
    kw = str(keyword).lower()
    results = [p for p in inventory if kw in p['code'].lower() or kw in p['name'].lower()]
    return results




def main():
    
    global inventory, transactions

    # copy past this to terminal:
    # python ummart.py Sam
    # replace Sam with your name
    if len(sys.argv) > 1:
        name = ' '.join(sys.argv[1:]).strip()
        if name:
            print(f"Hello, {name}! Welcome to UM MiniMart.")
    # ======================================================

    while True:

        print("\n[1] View Products")
        print("[2] Add Product")
        print("[3] Update Stock")
        print("[4] Purchase Product")
        print("[5] Delete Product")
        print("[6] Search Product")
        print("[0] Exit")


        choice = input("Select an option: ")


        if choice == "1":
            display_inventory()


        elif choice == "2": # [2] Add Product
            
            try:
                code = input("Product code (e.g. P00X): ").strip().upper()
                name = input("Name: ").strip()
                price = float(input("Price: "))
                stock = int(input("Initial stock (1): ") or 1) # NGL dapat 1 ang default stock

                item = add_product(code, name, price, stock) # def add_product used here
                print(f"\nAdded: {item['code']} - {item['name']} at PHP {item['price']:.2f} with stock of {item['stock']}")

            except Exception as e:
                print("Error adding product:", e)



        elif choice == "3": # [3] Update Stock

            try:
                code = input("Product code: ").strip().upper()
                quantity = int(input("Change in quantity (ex: 1 to add, -1 to remove): "))

                item = update_stock(code, quantity) # def update_stock(code, quantity) used here
                print(f"Updated stock for {item['code']}: {item['stock']}")

            except Exception as e:
                print("Error updating stock:", e)



        elif choice == "4": # [4] Purchase Product

            try:
                code = input("Product code: ").strip().upper()
                quantity = int(input("Quantity: "))

                purchase_product(code, quantity) # def purchase_product(code, quantity) used here

            except Exception as e:
                print("Error processing purchase:", e)



        elif choice == "5": # [5] Delete Product

            try:
                code = input("Product code to delete: ").strip().upper()
                removed = delete_product(code)
                print(f"Deleted product: {removed['code']} - {removed['name']}")

            except Exception as e:
                print("Error deleting product:", e)



        elif choice == "6": # [6] Search Product
            
            keyword = input("Enter code or name keyword to search: ").strip()
            results = search_products(keyword)

            if not results:
                print("No products match your search.")
                
            else:
                print("Search results:")
                for p in results:
                    print(p)



        elif choice == "0":
            print("\nThank you for using the UM MiniMart System.\n")
            break


        else:
            print("\nInvalid option. Please try again.")

if __name__ == "__main__":
    main()