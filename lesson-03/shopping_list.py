items = []
while True:
    print("Shopping List")
    print("1. Add item\n2. Remove item\n3. Show list\n4. Quit.")
    while True:
        try:
            option = int(input("Select Any option from above list only (1,2,3,4) : "))
        except ValueError:
            print("Entered value is wrong Please check the list")
            continue
        else:
            if option not in [1,2,3,4]:
                print("Entered Item not in the list Please check the list")
                continue
            else:
                break
    if option == 1:
        # Add Item
        item = input("Enter Item name to add into list : ").strip()
        if item == "":
            print("Please enter a Item name, It can not be empty")
            continue
        items.append(item)
    elif option == 2:
        # Remove Item
        if len(items) == 0:
            print("No Items in the list please add items")
            continue
        else:
            for index, name in enumerate(items, start=1):
                print(f"{index}. {name}")

        while True:
            try:
                remove_item = int(input("Enter item number from list to remove the item from list : "))
            except ValueError:
                print("Wrong Value. Entered Item number not in the list Please check the list")
                continue
            else:
                if remove_item - 1 in range(0, len(items)):
                    break
                else:
                    print("Entered Item number not in the list Please check the list")
                    continue
        removed_item = items.pop(remove_item - 1)
        print(f"{remove_item}. {removed_item} has been removed from shopping list")
    elif option == 3:
        # Show Items
        if len(items) == 0:
            print("No Items in the list please add items")
            continue
        else:
            for index, name in enumerate(items, start=1):
                print(f"{index}. {name}")
    elif option == 4:
        # quit
        print("------------Quitting the application----------")
        break
