#instaniate (create the variables and 2D list of items for sale

total = 0
command = "yes"
found = False 
NumberOfItems = 0
items = [[2.4,12.99],[1.23, 45.99],[1.11, 14.95]]

# keep asking and checking for an ID in the items 2D list. If not found, found is set to false /
# so prints not found. If found QTY asked and simple calc to work out total to be accumulated

while command == "yes":
    ID = float(input("please enter ID to find"))
    for i in range(len(items)):
        if items [i][0] == ID:
            found = True
            qty = int(input("please enter qty"))
            total += qty * items[i][1]
            NumberOfItems += qty
    if found == False:
        print("item not found try again")
    else:
        command = input("enter yes to continue").lower()
        found = False
        
#anything other than yes then while loop exits and the total is printed.        
        
print("The total cost is £ ", total)