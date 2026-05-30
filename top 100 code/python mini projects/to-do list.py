to_do_list = []

print()

print("Choose the options")
print("1. Add to the list")
print("2. remove from the list")
print("3. show the list")
print("4. To Leave")


while True:

    choice = int(input("enter your option: "))

    if choice == 1:
        enter_item = input("Enter Your Items: ")
        to_do_list.append(enter_item)
    
    if choice == 2:
        remove_item = input()
        to_do_list.remove(remove_item)

    if choice == 3:
        print(*to_do_list, sep='\n')

    if choice == 4:
        print("Thanks for using my to-do list app")
        print("Come again if you want! Bye...!")
        break
