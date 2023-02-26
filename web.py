import streamlit as st
import functions as f
todos=f.getTodos()

def addTodo():
    todo = st.session_state["newTodo"] + "\n"
    todos.append(todo)
    f.writeTodos(todos)

st.title("My Todo App")
st.subheader("This is my first web app.")
st.write("This app helps to increase your productivity. Go ahead and try it!")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.writeTodos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo: ", placeholder="Write here the new todo..",
              on_change=addTodo, key="newTodo")

# st.session_state
