"""
Application Name: Lab2.py
Developer: Alfred Varghese Jose
Date: 09/21/2023

An application program for a Vehicle Dealership Inventory, where the users can add new vehicles to the inventory and display the existing inventory stock. 
"""

import random


# add vehicles to inventory
def inventory_add(inventory):
    
    print("Adding vehicle in existing stock of vehicles .. .. ..")

    vehicle_make = input("\nEnter vehicle make:\t")
    vehicle_color = input("\nEnter color of the vehicle:\t")
    vehicle_vin = input("\nEnter five charecters (alpha/numeric) part of vin number:\t")
    vehicle_price = input("\nEnter price of vehicle:\t")

    # append 4 random digits to VIN
    vehicle_vin = vehicle_vin.upper() + str(random.randrange(1000, 9999))

    if inventory:
        print("\nThere is inventory of vehicles - check for VIN number .. .. .. ..")
        if vehicle_vin in inventory:
            print(f"\nVehicle VIN in stock - not adding this VIN, {vehicle_vin}, vehicle to inventory .. .. ..")
        else:
            print(f"\nVehicle VIN not in stock - adding this VIN, {vehicle_vin}, vehicle to inventory .. .. ..")
            inventory = inventory + f";{vehicle_make},{vehicle_color},{vehicle_vin},{vehicle_price}"
            print(f"\nVehicle with VIN {vehicle_vin} added to the inventory .. .. ..")
    else:
        print("\nThere are no vehicles in inventiory .. Adding new vehicle . . .")
        inventory = inventory + f"{vehicle_make},{vehicle_color},{vehicle_vin},{vehicle_price}"

    return inventory


# display inventory stock
def inventory_display(inventory):
    
    if inventory:
        vehicles = inventory.split(';')
        author_display()
        print("\n%60s\n%s" % ("Vehicle Inventory in Stock", "#*"*60))
        print("\n%30s%30s%30s%30s" % ("Vehicle Make", "Vehicle Color", "Vehicle VIN", "Vehicle Price"))
        for vehicle in vehicles:
            vehicle = vehicle.split(',')
            print("\n%30s%30s%30s%30s" % (vehicle[0], vehicle[1], vehicle[2], vehicle[3]))
        print("#*"*60)
    else:
        print("There is no stock in the inventory .. .. ..")


# display author info
def author_display():

    print("\n%s\n%120s\n%120s\n%s" % ("#*"*60, "Alfred Varghese Jose", "N01619463","#*"*60))


if __name__ == '__main__':

    print(__doc__)

    inventory = ""
    choice = ""

    # display menu and accept choice
    while choice != 'end':

        print("\n\ta) Type 'add' to add a new vehicle in inventory/stock \n\tb) Type 'display' to display stock of vehicles \n\tc) Type 'end' to end the application \n")
        choice = input("Please enter your choice .....")
        choice = choice.lower()
        
        if choice == 'add':
            inventory = inventory_add(inventory)

        elif choice == 'display':
            inventory_display(inventory)

        elif choice == 'end':
            print("\nApplication ending now .. .. .. ..")

        else:
            print("\nEnter a valid choice from the menu .. .. ..")