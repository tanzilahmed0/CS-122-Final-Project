from taskmaster.storage import db_manager, create_user, get_user_by_username
from taskmaster.models import User
from taskmaster.app_state import app_state
import tkinter as tk
from taskmaster.gui.task_form import TaskForm

# Initialize DB
db_manager.init_db()

# Create/get user
user = get_user_by_username("testuser")
if user is None:
    user = User(username="testuser", display_name="Test User")
    create_user(user)
    print(f"Created user: {user}")
else:
    print(f"Using existing user: {user}")

# Set as current user
app_state.current_user = user

root = tk.Tk()
root.title("TaskForm Test")
root.geometry("300x200")

# Status label
status_label = tk.Label(root, text=f"Tasks in app_state: {len(app_state.tasks)}", font=("Arial", 12))
status_label.pack(pady=20)

def open_form():
    def on_save():
        # Update status label
        status_label.config(text=f"Tasks in app_state: {len(app_state.tasks)}")
        print(f"Task saved! Total tasks: {len(app_state.tasks)}")
        if app_state.tasks:
            latest_task = app_state.tasks[-1]
            print(f"Latest task: {latest_task.title} - {latest_task.priority} - {latest_task.category}")
    
    TaskForm(root, on_save=on_save)

tk.Button(root, text="Open Add Task Form", command=open_form, font=("Arial", 12)).pack(pady=10)
tk.Label(root, text="Fill out the form and click Save.\nCheck the console for results.", font=("Arial", 9)).pack(pady=10)

root.mainloop()

