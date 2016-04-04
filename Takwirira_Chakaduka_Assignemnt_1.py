"""function main()
	load items from file
	display welcome msg
	display menu
	get choice
	while choice not ‘q’
		if choice is ‘l’
			call load items()
		else if choice is ‘h’
			call item hire()
		else if choice is ‘r’
			return items
			display item returned
		else
			display error message (invalid choice)
		display menu
		get choice
	print farewell message

load items ()
myfile = open(“items.csv”,’r’)
data = myfile.read()
print(data)"""



Menu = "\nMenu:\n(L)ist all items\n(H)ire an item\n(R)eturn an item\n(A)dd new item to the stock\n(Q)uit"

def main():
    print(Menu)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == "L":
            load_items()
        elif choice == "H":
            hire_items()
        elif choice == "R":
            items_list = []
            item_name = input("Enter the name of the item")
            if item_name == " ":
                print("please enter name of item")
            else:
                items_list.append(item_name)
                break
            item_description = input("Description: ")
            if item_description == " ":
                print("Please enter description")
            else:
                items_list.append(item_description)
                break
            item_charges = float(input("price per day: "))
            if item_charges == "" or item_charges <=0:
                print("Please enter valid amount")
            else:
                items_list.append(item_charges)
                break
        elif choice == "A":
            items_list = []
            item_name = input("Enter the name of the item")
            if item_name == " ":
                print("please enter name of item")
            else:
                items_list.append(item_name)
                break
            item_description = input("Description: ")
            if item_description == " ":
                print("Please enter description")
            else:
                items_list.append(item_description)
                break
            item_charges = float(input("price per day: "))
            if item_charges == "" or item_charges <=0:
                print("Please enter valid amount")
            else:
                items_list.append(item_charges)
                break
        else:
            print("Invalid menu choice.")

        print(Menu)
        choice = input(">>> ")








"""This function will load items from file"""
def load_items():
    items_file = open("items.csv","r")
    count = 0
    items_file.seek()
    for row in items_file:
        print (row)



main()



def hire_items():
    print("Hire items")