FILEPATH = "todos.txt"

def getTodos(filepath=FILEPATH):
    """ Read a text file and return the list
    of to-do items """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def writeTodos(todos_args, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_args)

if __name__ == "__main__":
    print("Hello")
    print(getTodos())