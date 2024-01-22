FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read the tex file and return the list of to-do items. """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the tex file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
