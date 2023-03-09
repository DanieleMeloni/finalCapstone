# Import tabulate module to display the shoes data in better way(tables)
from tabulate import tabulate # I had some help from www.github.com
#========The beginning of the class==========
# Class that contains the data of shoes, has five parameter
class Shoe:
    # Initializer method
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    # Method that return the cost of iteam in float type    
    def get_cost(self):
        return float(self.cost)
        '''
        Add the code to return the cost of the shoe in this method.
        '''
    # Method that return the cost of iteam in float type  
    def get_quantity(self):
        return int(self.quantity)
        '''
        Add the code to return the quantity of the shoes.
        '''
    # Method that allow to print the object on the screen and write on the file (I had some help from www.pythontutorial.net)
    def __str__(self): 
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
# Declaration of a list, It will conatis all object from the "Shoe" class
shoe_list = [] 
#==========Functions outside the class==============
# Function that read the data from "inventory.txt" file, for each line (except the first), makes "Shoe" class object and store them in the the "list_s" list, 
# it doesn't take any parameter and return the "list_shoes" 
def read_shoes_data():
    # Declaration of a list, it will contain Shoe class object
    list_shoes = []
    # Declaration of a list, it will contain the split line from "inventory.txt file"
    line_split = [] 
    # Check if the file is in the folder and avoid file not found error by printing a message
    try:
        # Open the "inventory.txt" file only for read 
        file_inventory = open("inventory.txt", "r") 
        # For loop that read any single line from the "inventory.txt" file, convert them in "Shoe" class object, 
        # by assigns the values to "iteam" and add to the "list_shoes" list
        for i, line in enumerate(file_inventory): 
            if i > 0: #If statement that avoid the first line of the "inventory.txt" file              
                line_split = line.strip().split(",")
                iteam = Shoe(line_split[0], line_split[1], line_split[2], line_split[3], line_split[4]) 
                list_shoes.append(iteam) 
        file_inventory.close()
        # If statement that checks if the file is empty in that case print a message
        if list_shoes == []: 
            print ("The inventory.txt file is empty") 
    except FileNotFoundError: 
        print("File inventory.txt not found")        
    return list_shoes
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
# Function that allow the user to enter a shoe in the system, thake one parameter "list_s"
def capture_shoes(list_s):    
    
    # Declaration and assignment of string variable, it contains the country
    country = input("Please enter the country: ") 
    # Declaration of list, it will contain the codes of the "Shoe" class object in the list_s, it will be assign by the next for loop 
    list_code = []    
    for shoe in list_s: 
        list_code.append(shoe.code)
    
    # Ifinite loop that it breaks when the code entered is correct, if is wrong print messages that suggest to try again
    while True:       
        # Declaration and assignment of string variable it contais the new code 
        code = input("Please enter the code: ") 
        if code in list_code: # If statement that checks the uniqueness of the new code
            print("The code is already assigned, try again") 
        else: 
            if len(code) != 8: # If statment that checks if the code's length is 8 characters 
                print("The code's length needs to be 8 characters, try again")
            else: 
                break
    
    # Declaration and assignment of string variable, it contains the description of the product
    product = input("Please enter the product: ")
    
    # Infinite loop that check if the value insert for cost float variable is correct, whether is wrong print a message
    while True: 
        try: 
            # Declaration and assignment of float variable, it contais the costo of new "Shoe" class object
            cost = float(input("Please enter the cost: ")) 
            break 
        except ValueError: 
            print("Wrong value, try again")
    
    # Infinite loop that breaks when the value of quantity integer variable entered by the user is correct, 
    # when the value is wrog print a message that suggest try again
    while True: 
        try:  
            #Declaration and assignment of integer variable it contains the quantity of shoes
            quantity = int(input("Please enter the quantity: ")) 
            break 
        except ValueError:
            print("Wrong value, try again")
    
    # Open inventory.txt file to add the new "Shoe" class object to the file, 
    # first check if the file is empty and then add the first line(that explain the content of date in the file) after the new shoe and close the file
    file_inventory = open("inventory.txt", "a+") 
    if list_s == []: 
        file_inventory.write(f"Country,Code,Product,Cost,Quantity") 
    file_inventory.write(f"\n{country},{code},{product},{cost},{quantity}") 
    file_inventory.close() 
    
    # Declaration and assignment of "Shoe" class object by sending the values entered by the user and add the new "Shoe" class object to the list_s
    iteam = Shoe(country, code, product, cost, quantity) 
    list_s.append(iteam) 
    return list_s
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
# Function that show all "Shoe" class object in the shoe_list, by printing them in table way, it has one parameter the "list_send"
def view_all(list_send):    
    # Declaration of a list it contains the value of "Shoe" class objects in the list_send list, for display the values with the module tabulate 
    list_table = [] 
    # For loop that add the values in the 2d "list_table" list
    for shoe in list_send: 
        list_table.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    print(tabulate(list_table, headers=["Country", "Code", "Product", "Cost", "Quantity"], tablefmt="grid"))
    
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
# Function that display the iteam with the lowest stock and ask to the user whether wants to add a quantity, 
# if the answer is positive it asks the quantity to add, it has one parameter is the shoe_list(list_send)
def re_stock(list_send):    
    
    # Declaration and assignment of list it contains two value the first is the quantity of the first element in the "list_send" the second is the position index "0"
    min_quant = [(list_send[0].get_quantity()), 0] 
    # For loop that check which iteam in the "list_send" has the lowest quantity and assign is value plus the index(position) to the "min_quant" variable
    for i, shoe in enumerate(list_send): 
        if min_quant[0] > shoe.get_quantity(): 
            min_quant = [shoe.get_quantity(), i]
    # Display a video the lowest quantity whith the name of the product
    print(f"The shoes with the lowest quantity are {list_send[min_quant[1]].product} with {min_quant[0]} pairs") 
   
    # Infinite loop that breaks if the user entered the right value in the system for the "answer" string variable, it takes only two value "yes" or "no"
    while True: 
        answer = input("Would you like add some quantity? Please answer with yes or no: ")         
        # When the user answer "yes", it start a infinite loop that ask for the quantity to add, if the vlaue entered by the user is not a correct integer 
        # it doesn't breaks the loop and a message it suggests to try again, when the loop breaks display a message that say the quantity ha been update 
        if answer.lower() == "yes":            
            while True: 
                try: 
                    # Declaration and assignment of integer variable, it contains the new add quantity value
                    new_quantity = int(input("Please enter the quantity would you like to add: ")) 
                    break 
                except ValueError:  
                    print("Wrong value, try again")
            
            # Assignment of the new quantity to the quantity of the iteam with the lowest quantity       
            new_quantity += min_quant[0] 
            list_send[min_quant[1]].quantity = new_quantity 
            
            # Open the "inventory.txt" file for writing, it will save the new quantity by rewriting all file and closing at the end
            file_inventory = open("inventory.txt", "w") 
            file_inventory.write(f"Country,Code,Product,Cost,Quantity") # Write the first line
            for line in list_send: # For loop that write every single line in the file
                file_inventory.write(f"\n{line.country},{line.code},{line.product},{line.cost},{line.quantity}") 
            file_inventory.close() 
            print("Quantity has been updated")            
            break
        # If the use enter "no" it will display a message and it will come back to the main menu 
        elif answer.lower() =="no": 
            print("Thank you")
            break 
        else:
            print("Wrong choise, try again")
    
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
# Function that display an iteam from the "shoe_list" in user friendy manner, it has one parameter the "shoe_list"("list_send")
def seach_shoe(list_send):    
    # Infinite loop that break when the user enter a code memorize in the system
    while True: 
        # Declaration of integer variable, it will be necessary to check if the code is inside or not 
        contactor = 0 
        # Declaration and assignment of string variable, it contains the code to research
        code = input("Please enter the shoe's code: ") 
        # For loop that checks for any iteams in the "list_send" if the code is the same as the one entered by the user,
        # in that case it will print the shoe iteam in friendly user manner
        for shoe in list_send:             
            if shoe.code == code:
                print(f"""
Country:    {shoe.country}
Code:       {shoe.code}
Product:    {shoe.product}
Cost:       {shoe.cost}
Quantity:   {shoe.quantity}  """)               
                break
            contactor += 1      
        # If statement that check if "contactor" is equal to the lenght of "list_send", whether true the code is not in the list so it print a message 
        if contactor == len(list_send): 
            print ("Code not found, try again")     
        break
    
    
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
# Function that calculate and display the value of each iteam in the "list_send", the value is the multiplay by the cost and the quantity
def value_per_item(list_send):
    # Declaration of a list that it will contais the values for the print
    list_table = [] 
    # For loop that add to the "list_table" all relevant value  from the "list_send" 
    for shoe in list_send: 
        list_table.append([shoe.code, shoe.product, (shoe.get_cost() * shoe.get_quantity())]) 
    print(tabulate(list_table, headers=["Code", "Product", "Value"], tablefmt="grid"))  
    
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
# Function that find the iteam with the highest quantity from "shoe_list"("list_send") and it displays a video, it has one parameter
def highest_qty(list_send):
    # Declaration and assignment of list, it contains the the quantity and the index position of the first iteam in the "list_send"
    max_quant = [(list_send[0].get_quantity()), 0] 
    # For loop that check any iteam in the "list_send" for found the shoe with the high quantity,
    # and assignment to the "max_quant" the highest quantity in position 0 and index in position 1 (to recover the name of the product)
    for index, shoe in enumerate(list_send): 
        if max_quant[0] < shoe.get_quantity(): 
            max_quant = [shoe.get_quantity(), index] 
    print(f"The shoe with the highest quantity is {list_send[max_quant[1]].code} {list_send[max_quant[1]].product} with {max_quant[0]} pairs, this shoe as being for sale.")
    
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
# Infinite loop that display the main menu, It breaks when the user chooses the option 2exit"
while True: 
    print("""
Please choose one option below:
r - read shoes data
c - capture_shoes
v - view all iteams
rs - restock
s - search shoe
vi - value per iteam
h - highest quantity
e - exit""")
    # Declaration and assignment of string variable, it contains the user choise
    choose = input(": ").lower() 

    # If statement option "r" load the data on the "shoe_list" and print that list has been loaded if the inventory.txt file is not empty or not found  
    if choose == "r":
        # Assignment of "shoe_list" by call the "read_shoes_data" function
        shoe_list = read_shoes_data() 
        if shoe_list != []: 
            print("List has been loaded") 
    
    # Eliff statement option "c", enter a new shoe in the system and print a message "Shoe has been recorded", 
    # first load "shoe_list" and after add the new shoe to the "shoe_list"
    elif choose == "c":         
        shoe_list = read_shoes_data() 
        shoe_list = capture_shoes(shoe_list)        
        print("Shoe has been recorded") 
    
    # Eliff statement option "v", show all shoes, first it assigns of "shoe_list" by call the "read_shoes_data" function
    # and after call the "view_all" function
    elif choose == "v": 
        shoe_list = read_shoes_data()
        view_all(shoe_list)

    # Eliff statement option "rs", restock a shoe, first it assigns of "shoe_list" by call the "read_shoes_data" function, 
    # after checks if the shoe_list is not empty if is true call the function "re_stock", it has one argument the "shoe_list"
    elif choose == "rs":     
        shoe_list = read_shoes_data() 
        if shoe_list != []: 
            re_stock(shoe_list) 

    # Eliff statement option "s", serch a shoe, first it assigns of "shoe_list" by call the "read_shoes_data" function,
    # after checks if the shoe_list is not empty if is true calls the "seach_shoe" function, it has one argument the "shoe_list"
    elif choose == "s":
        shoe_list = read_shoes_data() 
        if shoe_list != []: 
            seach_shoe(shoe_list) 

    # Eliff statement option "s", it calculates the value of each iteam, by calling the "value_per_item" function and send one argument to the function  
    # but first it assigns of "shoe_list" by call the "read_shoes_data" function,
    elif choose == "vi":
        shoe_list = read_shoes_data() 
        value_per_item(shoe_list) 
    
    # Eliff statement option "s", display the shoe with the highest quantity, first it assigns of "shoe_list" by call the "read_shoes_data" function,
    # after checks if the shoe_list is not empty if is true calls the "highest_qty" function, it has one argument the "shoe_list"
    elif choose == "h": 
        shoe_list = read_shoes_data() #Assignment of "shoe_list" by call the "read_shoes_data" function
        if shoe_list != []: 
            highest_qty(shoe_list) 
    
    elif choose == "e": 
        print("Good bye!") 
        break 
    
    else:
        print("Wrong choise! Try again")