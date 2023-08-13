contact = {}


def display():
    print("\nName\t|\t the number")
    print("-----" * 8)
    for key, value in contact.items():
        print(f"{key}\t|\t{value}")


n = True
while n == True:
    print("  1- choose number one to add new user")
    print("  2- choose number two to search the user")
    print("  3- choose number three to remove the user")
    print("  4- choose number four to show the user")
    print("  5- choose number five to exit")

    choice = int(input("your choice is : "))

    if choice == 1:
        print("add new user")
        user_name = input("please enter your name : ")
        phone = input("enter your namber: ")
        contact[user_name] = phone
        print("Saved successfully")
        print("-" * 50)

    elif choice == 2:
        search_name = str(input("please enter the name : "))
        if search_name in contact:
            print(f" The number for {search_name} is {contact[search_name]}")
            print("-" * 50)

        else:
            print(" No Found ")
            print("-" * 50)
    elif choice == 3:
        deleted_contact = input("Enter the name to delete it ")
        if deleted_contact in contact:
            data = contact.pop(deleted_contact)
            print(data)
            display()
            print("Deleted successfully ")
            print("-" * 50)

        else:
            print(" No found ")
            print("-" * 50)

    elif choice == 4:
        if not contact:
            print(" There is no contact")
            print("-" * 50)

        else:
            display()
            print("-" * 50)
    elif choice == 5:
        n == False
        break
