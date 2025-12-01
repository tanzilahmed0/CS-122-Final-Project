# Add/Edit task dialog

import tkinter as tk
from tkinter import ttk
from taskmaster.config import PRIORITIES
from taskmaster.models import Task
from taskmaster.storage import create_task
from taskmaster.app_state import app_state
from taskmaster.utils import parse_due_date


class TaskForm(tk.Toplevel):
    """Dialog to add or edit a task."""
    
    def __init__(self, parent, on_save=None, task=None):
        """
        Initialize TaskForm.
        
        Args:
            parent: Parent widget
            on_save: Callback function to call after saving
            task: Task object to edit (None for add mode)
        """
        super().__init__(parent)
        self.on_save = on_save
        self.task = task
        
        self.title("Add Task" if task is None else "Edit Task")
        self.geometry("400x400")
        
        self._build_ui()
    
    def _build_ui(self):
        """Build the task form UI."""
        # Title field
        tk.Label(self, text="Title:", font=("Arial", 10)).pack(pady=(10, 0), padx=10, anchor=tk.W)
        self.title_entry = tk.Entry(self, font=("Arial", 10), width=40)
        self.title_entry.pack(pady=5, padx=10)
        
        # Description field
        tk.Label(self, text="Description:", font=("Arial", 10)).pack(pady=(10, 0), padx=10, anchor=tk.W)
        self.description_text = tk.Text(self, font=("Arial", 10), width=40, height=5)
        self.description_text.pack(pady=5, padx=10)
        
        # Due date field
        tk.Label(self, text="Due Date (YYYY-MM-DD):", font=("Arial", 10)).pack(pady=(10, 0), padx=10, anchor=tk.W)
        self.due_date_entry = tk.Entry(self, font=("Arial", 10), width=40)
        self.due_date_entry.pack(pady=5, padx=10)
        
        # Priority dropdown
        tk.Label(self, text="Priority:", font=("Arial", 10)).pack(pady=(10, 0), padx=10, anchor=tk.W)
        self.priority_combo = ttk.Combobox(self, values=PRIORITIES, state="readonly", font=("Arial", 10), width=38)
        self.priority_combo.set("Medium")
        self.priority_combo.pack(pady=5, padx=10)
        
        # Category field
        tk.Label(self, text="Category:", font=("Arial", 10)).pack(pady=(10, 0), padx=10, anchor=tk.W)
        self.category_entry = tk.Entry(self, font=("Arial", 10), width=40)
        self.category_entry.pack(pady=5, padx=10)
        
        # Buttons frame
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Save", font=("Arial", 10), command=self._on_save_click, width=10).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Cancel", font=("Arial", 10), command=self._on_cancel_click, width=10).pack(side=tk.LEFT, padx=5)
    
    def _on_save_click(self):
        """Handle Save button click."""
        if self.task is None:
            # Add mode: create new task
            self._save_new_task()
        else:
            # Edit mode: update existing task (not implemented yet)
            pass
    
    def _save_new_task(self):
        """Create a new task and save to database."""
        # Read fields
        title = self.title_entry.get().strip()
        description = self.description_text.get("1.0", tk.END).strip()
        due_date_str = self.due_date_entry.get().strip()
        priority = self.priority_combo.get()
        category = self.category_entry.get().strip()
        
        # Validate title
        if not title:
            return
        
        # Parse due date
        due_date = parse_due_date(due_date_str)
        
        # Create Task object
        task = Task(
            user_id=app_state.current_user.id,
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            status="Pending",
            category=category
        )
        
        # Save to database
        create_task(task)
        
        # Add to app state
        app_state.tasks.append(task)
        
        # Call on_save callback if provided
        if self.on_save:
            self.on_save()
        
        # Close dialog
        self.destroy()
    
    def _on_cancel_click(self):
        """Handle Cancel button click."""
        self.destroy()

