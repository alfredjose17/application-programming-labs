"""
Application Name: Lab4.py
Developer: Alfred Varghese Jose
Date: 09/28/2023

An application program for a Warehouse Inventory, where the users can add new items to the inventory, display the existing inventory stock, search for an item from the inventory and purchase an item from the inventory. 
"""


# add vehicles to inventory
def inventory_add(inventory):

    item_name = input("\nEnter item name:\t").upper()
    item_sn = input("\nEnter Item Serial number ... a 5-charecters, alpha-numeric string:\t").upper()
    while True:
        if item_sn.isalnum() and len(item_sn) == 5:
            break
        else:
            print("\nInvalid Item Serial Number .. .. .. ..")
            item_sn = input("\nEnter Item Serial number ... a 5-charecters, alpha-numeric string:\t").upper()
    item_price = float(input("\nEnter price of item:\t$"))
    item_quantity = int(input("\nEnter Quantity of item - integer value :\t"))


    item = []
    item.append(item_name)
    item.append(item_sn)
    item.append(item_price)
    item.append(item_quantity)

    if inventory:
        if item_sn in inventory:
            if item_name == inventory[item_sn][0]:
                inventory[item_sn][2] = item_price
                inventory[item_sn][3] += item_quantity
                print("\nItem name and serial number of item matched .. .. .. ..\nAdding item in the items inventory - with updated quantity")
            else:
                print("\nItem serial number matched but name of item did not match .. ..\nItem information is not updated in the item inventory .. .. .. ..")
        else:
            print("\nItem was not in the list - adding new item to the list .. .. ..")
            inventory[item_sn] = item
    else:
        print("\nInventory of item is empty - add a new item")
        inventory[item_sn] = item


# display inventory stock
def inventory_display(inventory):
    
    if inventory:
        author_display()
        print("\n%60s\n%s" % ("Warehouse Inventory", "#*"*60))
        print("\n%30s%30s%30s%30s" % ("Item Name", "Item Serial Number", "Item Price", "Item Quantity"))
        for item in inventory.values():
            print("\n%30s%30s%30s%30s" % (item[0], item[1], "$%.2f" % item[2], item[3]))
        print("#*"*60)
    else:
        print("There are no items in the inventory to display .. .. ..")


# display author info
def author_display():

    print("\n%s\n%120s\n%120s\n%s" % ("#*"*60, "Alfred Varghese Jose", "N01619463","#*"*60))


# search for item in the inventory
def inventory_search(inventory):

    if inventory:
        item_sn = (input("\nEnter serial number of items to purchase:\t")).upper()
        if item_sn in inventory:
            inventory_display({item_sn: inventory[item_sn]})
        else:
            print("Item is not available in inventory .. .. ..")  
    else:
        print("Items inventory is empty - cannot search an item in the Items inventory")


# purchase an item from inventory
def inventory_purchase(inventory, sales):
    
    if inventory:
        inventory_display(inventory)
        item_sn = (input("\nEnter serial number of items to purchase:\t")).upper()
        item_quantity = int(input("Enter quantity of items to purchase:\t"))
        if item_sn in inventory:
            print("\nItem is in stock in item's inventory .. .. ..")    
            if inventory[item_sn][3] >= item_quantity:
                print("Enough quantity in stock .. .. ..")
                if item_sn in sales:
                    print("Item already listed in sales invoice .. updating quantity of item")
                    sales[item_sn][3] += item_quantity
                else:
                    print("Item is not listed in sales invoice .. adding new item in sales invoice")
                    sales[item_sn] = inventory[item_sn][:]
                    sales[item_sn][3] = item_quantity
                if inventory[item_sn][3] == item_quantity:
                    print("After this sale - stock reached limit of zero\nRemoving item information from the inventory list .. .. ..")
                    inventory.pop(item_sn)
                else:
                    inventory[item_sn][3] -= item_quantity
            else:
                print("Not enough quantity in stock ..\nHope you will visit our warehouse soon .. ..")
        else:
            print(f"\nWe do not carry item with serial number {item_sn} in stock .. .. .. \nPlease visit us at a later time.")
    else:
        print("\nThere are no items to purchase from the inventory .. ..\nDisplaying contents from sales invoice .. ..")
    sales_display(sales)


# display sales invoices
def sales_display(sales):
    
    if sales:
        total_price = 0
        total_tax = 0

        author_display()
        print("\n%60s\n%s" % ("Sales Invoices", "#*"*60))
        print("\n%30s%30s%30s%30s" % ("Item Name", "Item Serial Number", "Item Price", "Item Quantity"))
        for item in sales.values():
            print("\n%30s%30s%30s%30s" % (item[0], item[1], "$%.2f" % item[2], item[3]))
            total_price += item[2]*item[3]
            total_tax += item[2]*item[3]*0.13
        print("\n%120s\n%120s\n%120s" % ("Total price paid for computers: $%.2f" % total_price, "Tax amount paid: $%.2f" % total_tax, "Total amount paid including taxes and price of products: $%.2f" % (total_price + total_tax)))
    else:
        print("There are no items in the sales invoice - yet ..")



if __name__ == '__main__':

    print(__doc__)

    inventory = {}
    sales = {}
    choice = ""

    # display menu and accept choice
    while True:

        print("\n\ta) Enter 'Add Item' to add item in the inventory \n\tb) Enter 'Display' to display all items \n\tc) Enter 'Search' to search an item \n\td) Enter 'Purchase' to buy an item and create invoice \n\te) Enter 'End' to end the application \n")
        choice = input("Enter your choice ... ...")
        choice = choice.lower()
        
        if choice == 'add item' or choice == 'a':
            inventory_add(inventory)

        elif choice == 'display' or choice == 'b':
            inventory_display(inventory)

        elif choice == 'search' or choice == 'c':
            inventory_search(inventory)

        elif choice == 'purchase' or choice == 'd':
            inventory_purchase(inventory, sales)

        elif choice == 'end' or choice == 'e':
            print("\nApplication ending now .. .. .. ..")
            break

        else:
            print("\nPlease enter a valid choice from the menu .. .. ..")