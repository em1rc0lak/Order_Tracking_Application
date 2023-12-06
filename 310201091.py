#Function to read the text files and create the lists
def prepare_info(file_name,user_selection = None,):
    final_list = []
    with open(file_name,'r') as file:    
        for line in file:
            line = line.strip("# \n").split(";")
            if user_selection == None:
                final_list.append(line)
            elif line[0] == str(user_selection):
                final_list.append(line)   
    return final_list

#Function to print the choices
def print_menu(list_name):    
    for index, element in enumerate(list_name):
        print(f"{index+1}. {element[1]}")
    
#Function to get the user input
def get_user_input(section):
    choice = int(input(f"Please select a {section}: "))
    print()
    return choice

#Main function
def main():

    #Print the welcome message 
    print("-"*30)
    print("Welcome to the Store")
    print("-"*30)
    
    #Create the order list and the total price to print at the end
    total_order = []
    total_price = 0.0 
    
    while True:
        
        #keep track of the current order
        current_order = []

        #Print the categories and get the user input
        category_list = prepare_info("categories.txt")
        print_menu(category_list)
        category_choice = get_user_input("category")
        
        current_order.append(category_list[category_choice-1][1])

        #Category name
        print("-"*30)
        print(category_list[category_choice-1][1])
        print("-"*30)

        #Print the products and get the user input
        product_list = prepare_info("products.txt",category_choice)
        print_menu(product_list)
        product_choice = get_user_input("product")
        product_code = product_list[product_choice-1][2]
        
        current_order.append(product_list[product_choice-1][1])

        #Product name
        print("-"*30)
        print(product_list[product_choice-1][1])
        print("-"*30)

        #Print the portions and get the user input
        portion_list = prepare_info("portions.txt",product_code)
        print_menu(portion_list)
        portion_choice = get_user_input("portion")

        current_order.append(portion_list[portion_choice-1][1])
        current_order.append(portion_list[portion_choice-1][2])
        
        total_price += float(portion_list[portion_choice-1][2])

        #Add the current order to the total order
        total_order.append(current_order)

        #Check if the user wants to exit
        if input("Would you like to complete the order? (y/n): ") == "y":
            #Print the order user wants to complete        
            print()
            print("Order Recipe\n")
            print("="*75,end="\n\n")
            for i in range(len(total_order)):
                print(f"{total_order[i][0]:<22}   {total_order[i][1]:<32}   {total_order[i][2]:<6}   {total_order[i][3]}$")
            print("\n"+"="*75)
            print(f"Total: {total_price}$\n")            
            break
        else:
            print()
            #user wants to add more products      
            continue
main()


