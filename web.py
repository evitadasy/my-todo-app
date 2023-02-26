import streamlit as st
import functions as f
todos=f.getTodos()

st.set_page_config(layout="wide")

def addTodo():
    todo = st.session_state["newTodo"] + "\n"
    todos.append(todo)
    f.writeTodos(todos)

st.title("My Todo App")
st.subheader("This is my first web app.")
st.write("This app helps to increase your <b>productivity</b>. Go ahead and try it!<br><br>", unsafe_allow_html=True)


for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.writeTodos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.write("<br>", unsafe_allow_html=True)


st.text_input(label="Enter a todo: ", placeholder="Write here the new todo..",
              on_change=addTodo, key="newTodo")
# st.session_state
