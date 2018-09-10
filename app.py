from model import *
if __name__=='__main__':
    print ("Welcome to the Todo application Choose your option")
    print ("\n 1. Create Todo \n 2. Find specific todo .\n  3. Delete specific todo .\n 4. Update a specific todo  \n 5. clear the todo list")
    
    selection = int(input("Enter input "))  

    if selection == 1:
        
        title = input("Enter your title \n >>> ")
        description = input("Enter your item \n >>> ")
        create_todo(title, description)

    if selection == 2:
        
        print ("\t ....Finding a items....")
        item = input("Enter your title name \n >>> ")
        find_todo(item)

    if selection == 3:
    
        title = input("Enter your title to be deleted.\n >>> ")
        delete_todo(title)
        
        
    if selection == 4:
        title= input("Enter your title name\n >>> ")
        item= input("Enter your new item name\n >>> ")
        edit_todo(title,item)
        
    
    if selection == 5:
        del_todo()   
        

    

