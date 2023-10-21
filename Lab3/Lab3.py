"""
Application Name: Lab3.py
Developer: Alfred Varghese Jose
Date: 09/21/2023

An application program for a Warehouse Inventory, where the users can add new items to the inventory, display the existing inventory stock and search for an item from the inventory. 
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
        item_found = 0
        for x in range(len(inventory)):
            if item_sn == inventory[x][1]:
                if item_name == inventory[x][0]:
                    inventory[x][2] = item_price
                    inventory[x][3] += item_quantity
                    item_found = 2
                    break
                else:
                    item_found = 1
                    break
        if item_found == 2:
            print("\nItem name and serial number of item matched .. .. .. ..\nAdding item in the items inventory - with updated quantity")
        elif item_found == 1:
            print("\nItem serial number matched but name of item did not match .. ..\nItem information is not updated in the item inventory .. .. .. ..")
        else:
            print("\nItem was not in the list - adding new item to the list .. .. ..")
            inventory.append(item)
    else:
        print("\nInventory of item is empty - add a new item")
        inventory.append(item)


# display inventory stock
def inventory_display(inventory):
    
    if inventory:
        author_display()
        print("\n%30s%30s%30s%30s" % ("Item Name", "Item Serial Number", "Item Price", "Item Quantity"))
        for item in inventory:
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
        search_item = input("\nEnter serial number to search:\t")
        item_found = False
        for item in inventory:
            if search_item == item[1]:
                item_found = True
                inventory_display([item])
        if not item_found:
            print("Item is not available in inventory .. .. .. .. ..")  
    else:
        print("Items inventory is empty - cannot search an item in the Items inventory")


if __name__ == '__main__':

    print(__doc__)

    inventory = []
    choice = ""

    # display menu and accept choice
    while True:

        print("\n\ta) Enter 'Add Item' to add item in the inventory \n\tb) Enter 'Display' to display all items \n\tc) Enter 'Search' to search an item \n\td) Enter 'End' to end the application \n")
        choice = input("Enter your choice ... ...")
        choice = choice.lower()
        
        if choice == 'add item' or choice == 'a':
            inventory_add(inventory)

        elif choice == 'display' or choice == 'b':
            inventory_display(inventory)

        elif choice == 'search' or choice == 'c':
            inventory_search(inventory)

        elif choice == 'end' or choice == 'd':
            print("\nApplication ending now .. .. .. ..")
            break

        else:
            print("\nPlease enter a valid choice from the menu .. .. ..")