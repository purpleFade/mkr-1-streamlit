import streamlit as st

st.set_page_config(page_title="Чекліст завдань")

# Ініціалізація списку завдань у session_state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("Чекліст завдань")

# Поле для додавання нового завдання
new_task = st.text_input("Введіть нове завдання:")
if st.button("Додати завдання"):
    if new_task.strip():
        st.session_state.tasks.append({"title": new_task.strip(), "done": False})

# Виводимо список завдань
st.write("### Список завдань:")
for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([0.1, 0.9])

    # Чекбокс для позначення виконання
    with col1:
        checked = st.checkbox("", value=task["done"], key=f"checkbox_{i}", label_visibility="hidden")

    if checked != task["done"]:
        st.session_state.tasks[i]["done"] = checked

    with col2:
        task_text = task["title"]
        if task["done"]:
            st.markdown(f"~~{task_text}~~")
        else:
            st.write(task_text)

    delete_button = st.button("Видалити", key=f"del_{i}")
    if delete_button:
        st.session_state.tasks.pop(i)
