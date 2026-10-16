items = []
while True:
    print("Shopping List")
    print("1. Add item\n2. Remove item\n3. Show list\n4. Quit.")
    while True:
        try:
            option = int(input("Select Any option from above list only (1,2,3,4)"))
        except ValueError:
            continue
        else:
            if option not in [1,2,3,4]:
                continue
            else:
                break
    if option == 1:
        # Add Item
        item = input("Enter Item name to add into list : ")
        items.append(item)
    elif option == 2:
        # Remove Item
        if len(items) == 0:
            print("No Items in the list please add items")
            continue
        else:
            for index, item in enumerate(items, start=1):
                print(f"{index}. {item}")

        remove_item = input("Enter item name from list to remove the item from list")

        if remove_item in items:
            items.remove(remove_item)
            print(f"{remove_item} has been removed from shopping list")
        else:
            print("Entered Item not in the list")
    elif option == 3:
        # Show Items
        if len(items) == 0:
            print("No Items in the list please add items")
            continue
        else:
            for index, item in enumerate(items, start=1):
                print(f"{index}. {item}")
    elif option == 4:
        # quit
        print("------------Quitting the application----------")
        break
    else:
        print("Select Any option from above list only (1,2,3,4)")
        continue

