import tkinter as tk
from taskmaster.gui.main_view import MainView
from taskmaster.models import Task

root = tk.Tk()
root.title("MainView Test")
main_view = MainView(root)
main_view.pack(fill=tk.BOTH, expand=True)

# Create dummy tasks
tasks = [
    Task(user_id=1, title='Task 1', description='Desc 1', due_date=None, priority='High', status='Pending', category='School', id=1),
    Task(user_id=1, title='Task 2', description='Desc 2', due_date=None, priority='Low', status='Completed', category='Work', id=2)
]

main_view.populate_tasks(tasks)

root.mainloop()