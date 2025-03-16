
filepath='toto.txt'
def get_todo(filepath='toto.txt'):
    with open(filepath,'r') as file:
        todo=file.readlines()
        return todo

def set_todo(todos,filepath='toto.txt'):
    with open(filepath,'w') as file:
        file.writelines(todos)