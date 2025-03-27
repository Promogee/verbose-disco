import streamlit as st
import function

todos=function.get_todo()
st.title('My Todo App')
def add_todo():
    todo=st.session_state['new_todo']+'\n'
    for item in todos:
        if item ==todo:
            st.toast('you cannot put the same todo twice')

        else:
            todos.append(todo)
            function.set_todo(todos)

for index, todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        function.set_todo(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input('enter a todo',placeholder='add a new todo',key='new_todo',on_change=add_todo)

