#Read the text files and convert them to lists
def prepare_info(file_name):
    final_list = []
    with open(file_name,'r') as file:    
        for line in file:
            line = line.strip("# \n")
            line = line.split(";")
            final_list.append(line)    
    return final_list    

#Print the choices
def print_menu(list_name):    
    for i in range(len(list_name)):
        print(f"{i+1}. {list_name[i][1]}")
    
#Get the user input
def get_user_input(section):
    choice = int(input(f"Please select a {section}: "))
    print()
    return choice

#Main function
def main():
    #Create the lists of categories, products and portions
    categoryList = prepare_info("categories.txt")
    productList = prepare_info("products.txt")   
    portionList = prepare_info("portions.txt")

    #Print the welcome message 
    print("------------------------------------")
    print("Welcome to the Store")
    print("------------------------------------")
    
    #Create the order list and the total price to print at the end
    total_order = []
    total_price = 0 
    
    while True:

        current_order = []
        available_products = []
        available_portions = []

        #Print the categories and get the user input
        print_menu(categoryList)
        category_choice = get_user_input("category")
        
        #Add the category name to the current order list
        current_order.append(categoryList[category_choice-1][1])
        

        #Create the available products list according to the category choice   
        for i in range (len(productList)):
            if productList[i][0] == str(category_choice):
                available_products.append(productList[i])
        
        #Category name
        print("------------------------------------")
        print(categoryList[category_choice-1][1])
        print("------------------------------------")

        #Print the available products and get the user input    
        print_menu(available_products)
        product_choice = get_user_input("product")
        
        #Add the product name to the current order list
        current_order.append(available_products[product_choice-1][1])

        #Create the available portions list according to the product choice
        for i in range(len(portionList)):   
            if portionList[i][0] == available_products[product_choice-1][-1]:
                available_portions.append(portionList[i])

        #Product name 
        print("------------------------------------")
        print(categoryList[category_choice-1][1])
        print("------------------------------------")

        #Print the available portions and get the user input
        print_menu(available_portions)  
        portion_choice = get_user_input("portion")
        
        #Add the portion name and price to the current order list
        current_order.append(available_portions[portion_choice-1][1])
        current_order.append(available_portions[portion_choice-1][2])
        
        #Add the current price to the total price            
        total_price += float(available_portions[portion_choice-1][2])
        
        #Add the current order to the total order list
        total_order.append(current_order)

        #Check if the user wants to exit
        if input("Would you like to complete the order? (y/n): ") == "y":
            #Print the order user wants to complete        
            print()
            print("Order Recipe")
            print("=============================================================================",end="\n\n")
            for i in range(len(total_order)):
                print(f"{total_order[i][0]:<22}   {total_order[i][1]:<32}   {total_order[i][2]:<6}   {total_order[i][3]}$",end="\n\n")
            print("=============================================================================")
            print(f"Total: {total_price}$")            
            break
        else:      
            #user wants to add more products      
            continue

main()


