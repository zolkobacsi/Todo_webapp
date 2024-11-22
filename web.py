import streamlit as st
import functions


if "new_todo" not in st.session_state:
    st.session_state["new_todo"] = ""

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"].strip() + "\n"
    if todo != "\n" and todo not in todos:
        todos.append(todo)
        functions.write_todos(todos)
    st.session_state["new_todo"] = ""
    st.rerun=()
    


st.title("My todo app")
st.write("What you still need to do is:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun=()
st.rerun=()


st.text_input("Enter a todo", placeholder="Add a new todo here...",
              on_change=add_todo(), key="new_todo")
st.rerun=()



st.session_state