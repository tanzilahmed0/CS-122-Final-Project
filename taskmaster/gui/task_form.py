# Add/Edit task dialog

import tkinter as tk
from tkinter import ttk
from taskmaster.config import PRIORITIES
from taskmaster.models import Task
from taskmaster.storage import create_task, update_task
from taskmaster.app_state import app_state
from taskmaster.utils import parse_due_date

# Configure ttk style for better combobox appearance
style = ttk.Style()
style.theme_use('default')
style.configure('TCombobox', padding=5)


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
        self.geometry("550x650")
        
        self._build_ui()
        
        # If editing, pre-fill fields
        if self.task is not None:
            self._populate_fields()
    
    def _build_ui(self):
        """Build the task form UI."""
        # Title field
        tk.Label(self, text="Title:", font=("Arial", 11, "bold")).pack(pady=(15, 5), padx=20, anchor=tk.W)
        self.title_entry = tk.Entry(self, font=("Arial", 11), relief=tk.SOLID, bd=2)
        self.title_entry.pack(pady=5, padx=20, fill=tk.X, ipady=6)
        
        # Description field
        tk.Label(self, text="Description:", font=("Arial", 11, "bold")).pack(pady=(15, 5), padx=20, anchor=tk.W)
        self.description_text = tk.Text(self, font=("Arial", 11), relief=tk.SOLID, bd=2, height=6, wrap=tk.WORD)
        self.description_text.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)
        
        # Due date field
        tk.Label(self, text="Due Date (YYYY-MM-DD):", font=("Arial", 11, "bold")).pack(pady=(15, 5), padx=20, anchor=tk.W)
        self.due_date_entry = tk.Entry(self, font=("Arial", 11), relief=tk.SOLID, bd=2)
        self.due_date_entry.pack(pady=5, padx=20, fill=tk.X, ipady=6)
        
        # Priority dropdown
        tk.Label(self, text="Priority:", font=("Arial", 11, "bold")).pack(pady=(15, 5), padx=20, anchor=tk.W)
        priority_frame = tk.Frame(self, relief=tk.SOLID, bd=2)
        priority_frame.pack(pady=5, padx=20, fill=tk.X)
        self.priority_combo = ttk.Combobox(priority_frame, values=PRIORITIES, state="readonly", font=("Arial", 12), height=10)
        self.priority_combo.set("Medium")
        self.priority_combo.pack(fill=tk.BOTH, expand=True, ipady=8, padx=2, pady=2)
        
        # Category field
        tk.Label(self, text="Category:", font=("Arial", 11, "bold")).pack(pady=(15, 5), padx=20, anchor=tk.W)
        self.category_entry = tk.Entry(self, font=("Arial", 11), relief=tk.SOLID, bd=2)
        self.category_entry.pack(pady=5, padx=20, fill=tk.X, ipady=6)
        
        # Buttons frame
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        
        # Button styling
        button_config = {
            'font': ('Arial', 11, 'bold'),
            'relief': tk.RAISED,
            'bd': 2
        }
        
        tk.Button(button_frame, text="Save", command=self._on_save_click, bg='#4CAF50', fg='black', **button_config).pack(side=tk.LEFT, padx=5, ipadx=20, ipady=8)
        tk.Button(button_frame, text="Cancel", command=self._on_cancel_click, **button_config).pack(side=tk.LEFT, padx=5, ipadx=20, ipady=8)
    
    def _populate_fields(self):
        """Pre-fill fields with task data for edit mode."""
        # Set title
        self.title_entry.insert(0, self.task.title)
        
        # Set description
        self.description_text.insert("1.0", self.task.description)
        
        # Set due date
        if self.task.due_date:
            self.due_date_entry.insert(0, self.task.due_date.strftime("%Y-%m-%d"))
        
        # Set priority
        self.priority_combo.set(self.task.priority)
        
        # Set category
        if self.task.category:
            self.category_entry.insert(0, self.task.category)
    
    def _on_save_click(self):
        """Handle Save button click."""
        if self.task is None:
            # Add mode: create new task
            self._save_new_task()
        else:
            # Edit mode: update existing task
            self._update_existing_task()
    
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
    
    def _update_existing_task(self):
        """Update an existing task in the database."""
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
        
        # Update task attributes
        self.task.title = title
        self.task.description = description
        self.task.due_date = due_date
        self.task.priority = priority
        self.task.category = category
        
        # Call touch to update timestamp
        self.task.touch()
        
        # Save to database
        update_task(self.task)
        
        # Call on_save callback if provided
        if self.on_save:
            self.on_save()
        
        # Close dialog
        self.destroy()
    
    def _on_cancel_click(self):
        """Handle Cancel button click."""
        self.destroy()

