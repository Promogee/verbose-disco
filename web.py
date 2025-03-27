import streamlit as st
import function
todos=function.get_todo()

def add_todo():
    todo=st.session_state['new_todo']+'\n'
    todos.append(todo)
    function.set_todo(todos)
st.title('My Todo App')
for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        function.set_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input('enter a todo',placeholder='add a new todo',key='new_todo',on_change=add_todo)

