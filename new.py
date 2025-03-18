import FreeSimpleGUI as sc
from function import get_todo,set_todo

todos = get_todo()
label=sc.Text('type in a todo')
input_box=sc.InputText(tooltip='enter a todo',key='todo')
list_box=sc.Listbox(values=get_todo(),key='todos',enable_events=True,size=[45,15])
button=sc.Button('add')
edit_button=sc.Button('edit')
window=sc.Window('My todo App',layout=[[label],[input_box,button],[list_box,edit_button]],font=('sans-serif',15))

while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case 'add':
            todos=get_todo()
            new_todo=values['todo']+'\n'
            todos.append(new_todo)
            set_todo(todos)
            window['todos'].update(values=todos)
        case 'edit':
            new_todo=values['todo']
            print(new_todo)
            todo_to_edit=values['todos'][0]
            print(todo_to_edit)
            index_of_todo=todos.index(todo_to_edit)
            todos[index_of_todo]=new_todo+'\n'
            set_todo(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])

window.close()
# label=sc.Text('enter feet')
# label2=sc.Text('enter inches')
# input_box=sc.InputText(tooltip='enter feet')
# input_box2=sc.InputText(tooltip='enter inches')
# button=sc.Button('convert')
# window=sc.Window('converter',layout=[[label,input_box],[label2,input_box2],[button]],font=('sans-serif',20))
# window.read()
# window.close()
