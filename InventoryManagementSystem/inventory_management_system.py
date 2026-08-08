import os

FILE_NAME = "inventory.txt"


def add_product():
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = input("Enter Price: ")
    quantity = input("Enter Quantity: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{product_id},{product_name},{category},{price},{quantity}\n")

    print("\n✅ Product added successfully!\n")
def add_product():
    product_id = input("Enter Product ID: ")
    product_name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = input("Enter Price: ")
    quantity = input("Enter Quantity: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{product_id},{product_name},{category},{price},{quantity}\n")

    print("\n✅ Product added successfully!\n")


# 👇 ఇక్కడ paste చేయాలి

def view_products():
    if not os.path.exists(FILE_NAME):
        print("\nNo products found.\n")
        return

    with open(FILE_NAME, "r") as file:
        products = file.readlines()

    print("\n========== Product List ==========")

    for product in products:
        product = product.strip().split(",")

        print(f"Product ID   : {product[0]}")
        print(f"Product Name : {product[1]}")
        print(f"Category     : {product[2]}")
        print(f"Price        : ₹{product[3]}")
        print(f"Quantity     : {product[4]}")
        print("-" * 35)


# 👇 దీని తర్వాత while True వస్తుంది


while True:
    print("\n========== Inventory Management System ==========")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Buy Product")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_products()

    elif choice == "3":
        print("\nSearch Product feature will be added in the next step.\n")

    elif choice == "4":
        print("\nUpdate Product feature will be added in the next step.\n")

    elif choice == "5":
        print("\nDelete Product feature will be added in the next step.\n")

    elif choice == "6":
        print("\nBuy Product feature will be added in the next step.\n")

    elif choice == "7":
        print("\nThank you for using Inventory Management System!")
        break

    else:
        print("\nInvalid choice! Please try again.\n")