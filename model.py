

# creating an empty dictionary
todos ={}

title = str


def create_todo (title, description):
            todos[title] = description# add the title:item to the dictionary
           
def find_todo (title):   
    Todo = todos[title]
    print ( Todo )
def delete_todo (title):
    todos.pop(title)

def edit_todo(title,item):
    todos[title] = item
    print ("Todo item has been edited")

def del_todo ():
    todos.clear()
    print ("List has been successfully emptied")
