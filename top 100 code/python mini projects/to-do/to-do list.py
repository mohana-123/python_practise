print("Choose the options")
print("1. Add to the list")
print("2. remove from the list")
print("3. show the list")
print("4. To Leave")


def add_to_the_list(enter_item): #done
    with open('to-do/to_do_list.txt','a') as fa:
        contents = enter_item
        fa.write(contents + '\n')

def remove_item_list(remove_item): # done
    with open('to-do/to_do_list.txt','r') as fr:
        contents = fr.read().splitlines()
        if remove_item in contents:
            contents.remove(remove_item)

            with open('to-do/to_do_list.txt','w') as fw:
                fw.write('\n'.join(contents) + '\n')
        else:
            print("Not found")

def show_list(): #done
    with open('to-do/to_do_list.txt','r') as rr:
        content = rr.read()
        return content


while True:

    choice = int(input("enter your option: "))

    if choice == 1:
        enter_item = input("Enter Your Item: ")
        add_to_the_list(enter_item)
    
    if choice == 2:
        remove_item = input("Enter an item to remove: ")
        remove_item_list(remove_item)

    if choice == 3:
        print(show_list())

    if choice == 4:
        print("Thanks for using my to-do list app")
        print("Come again if you want! Bye...!")
        break
