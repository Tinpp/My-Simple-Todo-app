FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):  # default argumentin määritys. Se voidaan kuitenkin funktion kutsussa ohittaa.
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH): # default argumentti ei voi olla ensimmäinen.
    """ Write the to-do items in the text file. """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


print(__name__)

if __name__ == "__main__":  # __name__ saa arvon "main" ajetaan suoraan tässä scriptistä. Jos taas se ajetaan
    print("Hello")          # pää-ohjelmasta, niin se saa silloin arvon "functions".
    print(get_todos())