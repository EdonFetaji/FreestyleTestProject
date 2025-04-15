import streamlit as st
import requests
import pandas as pd
import os

API_HOST = os.getenv("API_HOST", "localhost")
API_PORT = os.getenv("API_PORT", "5000")
API_URL = f"http://{API_HOST}:{API_PORT}/tasks"

st.title("📝 To-Do List App")

# --- Add Task ---
st.subheader("➕ Add a New Task")
with st.form("add_task_form", clear_on_submit=True):
    name = st.text_input("Task Name")
    category = st.text_input("Category")
    description = st.text_area("Description")
    deadline = st.date_input("Deadline")
    priority = st.selectbox("Priority", [1, 2, 3, 4, 5])
    submit_add = st.form_submit_button("Add Task")
    if submit_add:
        response = requests.post(API_URL, json={
            "name": name,
            "category": category,
            "description": description,
            "deadline": str(deadline),
            "priority": priority
        })
        if response.status_code == 201:
            st.success("Task added successfully!")
        else:
            st.error("Failed to add task.")
        st.rerun()

# --- Fetch Tasks ---
st.subheader("📋 Task List")
try:
    tasks = requests.get(API_URL).json()
except:
    st.error("⚠️ Could not connect to the backend.")
    tasks = []

if tasks:
    for task in tasks:
        with st.expander(f"📌 {task['name']} (Priority {task['priority']})"):
            st.markdown(f"**Category:** {task['category']}")
            st.markdown(f"**Deadline:** {task['deadline']}")
            st.markdown(f"**Description:** {task['description']}")

            col1, col2 = st.columns([1, 1])

            # --- Edit Task Form ---
            with col1:
                if st.button(f"✏️ Edit Task {task['id']}"):
                    with st.form(f"edit_form_{task['id']}"):
                        new_name = st.text_input("Task Name", value=task["name"])
                        new_category = st.text_input("Category", value=task["category"])
                        new_description = st.text_area("Description", value=task["description"])
                        new_deadline = st.date_input("Deadline", pd.to_datetime(task["deadline"]))
                        new_priority = st.selectbox("Priority", [1, 2, 3, 4, 5], index=task["priority"] - 1)

                        submit_edit = st.form_submit_button("Update Task")
                        if submit_edit:
                            update = requests.put(f"{API_URL}/{task['id']}", json={
                                "name": new_name,
                                "category": new_category,
                                "description": new_description,
                                "deadline": str(new_deadline),
                                "priority": new_priority
                            })
                            if update.status_code == 200:
                                st.success("✅ Task updated!")
                                st.rerun()
                            else:
                                st.error("❌ Update failed.")

            # --- Delete Task ---
            with col2:
                if st.button(f"🗑️ Delete Task {task['id']}"):
                    delete = requests.delete(f"{API_URL}/{task['id']}")
                    if delete.status_code == 200:
                        st.success("🗑️ Task deleted successfully.")
                        st.rerun()
                    else:
                        st.error("❌ Failed to delete task.")
else:
    st.info("No tasks found.")
