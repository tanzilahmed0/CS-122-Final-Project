# Main task list view (CRUD + filters)

import tkinter as tk
from tkinter import ttk
from taskmaster.storage import get_tasks_for_user, delete_task, update_task
from taskmaster.app_state import app_state
from taskmaster.gui.task_form import TaskForm
from taskmaster.gui.reports_view import ReportsView


class MainView(tk.Frame):
    """Main task list view with CRUD and filters."""
    
    def __init__(self, parent):
        """
        Initialize MainView.
        
        """
        super().__init__(parent)
        self._build_ui()
    
    def _build_ui(self):
        """Build the main view UI layout."""
        # Top frame for filters
        filter_frame = tk.Frame(self)
        filter_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Status filter
        tk.Label(filter_frame, text="Status:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.status_filter = ttk.Combobox(filter_frame, values=["All", "Pending", "Completed"], state="readonly", width=15, font=("Arial", 10), height=10)
        self.status_filter.set("All")
        self.status_filter.pack(side=tk.LEFT, padx=5, ipady=3)
        
        # Priority filter
        tk.Label(filter_frame, text="Priority:", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        self.priority_filter = ttk.Combobox(filter_frame, values=["All", "Low", "Medium", "High"], state="readonly", width=15, font=("Arial", 10), height=10)
        self.priority_filter.set("All")
        self.priority_filter.pack(side=tk.LEFT, padx=5, ipady=3)
        
        # Treeview for task list
        tree_frame = tk.Frame(self)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create Treeview with columns
        self.tree = ttk.Treeview(tree_frame, columns=("Title", "Due Date", "Priority", "Status", "Category"), show="headings")
        
        # Define column headings
        self.tree.heading("Title", text="Title")
        self.tree.heading("Due Date", text="Due Date")
        self.tree.heading("Priority", text="Priority")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Category", text="Category")
        
        # Define column widths
        self.tree.column("Title", width=200)
        self.tree.column("Due Date", width=100)
        self.tree.column("Priority", width=80)
        self.tree.column("Status", width=100)
        self.tree.column("Category", width=100)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Button frame
        button_frame = tk.Frame(self)
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Button styling
        button_config = {
            'font': ('Arial', 10, 'bold'),
            'relief': tk.RAISED,
            'bd': 2
        }
        
        tk.Button(button_frame, text="Add Task", command=self._on_add_task, **button_config).pack(side=tk.LEFT, padx=5, pady=5, ipadx=10, ipady=5)
        tk.Button(button_frame, text="Edit Task", command=self._on_edit_task, **button_config).pack(side=tk.LEFT, padx=5, pady=5, ipadx=10, ipady=5)
        tk.Button(button_frame, text="Delete Task", command=self._on_delete_task, **button_config).pack(side=tk.LEFT, padx=5, pady=5, ipadx=10, ipady=5)
        tk.Button(button_frame, text="Complete Task", command=self._on_complete_task, **button_config).pack(side=tk.LEFT, padx=5, pady=5, ipadx=10, ipady=5)
        tk.Button(button_frame, text="Refresh", command=self._on_refresh, **button_config).pack(side=tk.LEFT, padx=5, pady=5, ipadx=10, ipady=5)
        tk.Button(button_frame, text="Reports", command=self._on_reports, **button_config).pack(side=tk.LEFT, padx=5, pady=5, ipadx=10, ipady=5)
    
    def populate_tasks(self, tasks):
        """
        Display a list of tasks in the Treeview.
        
        """
        # Clear existing rows
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Insert new rows
        for task in tasks:
    
            due_date_str = task.due_date.strftime("%m/%d/%Y") if task.due_date else ""
            
            # Insert row with task data
            self.tree.insert("", tk.END, iid=str(task.id), values=(
                task.title,
                due_date_str,
                task.priority,
                task.status,
                task.category or ""
            ))
    
    def get_filtered_tasks(self):
        """
        Filter tasks based on status and priority filters.

        """
        # Start with all tasks
        filtered = app_state.tasks[:]
        
        # Filter by status
        status_filter = self.status_filter.get()
        if status_filter != "All":
            filtered = [t for t in filtered if t.status == status_filter]
        
        # Filter by priority
        priority_filter = self.priority_filter.get()
        if priority_filter != "All":
            filtered = [t for t in filtered if t.priority == priority_filter]
        
        return filtered
    
    def refresh_tasks(self):
        """Reload tasks from database and update the view."""
      
        app_state.tasks = get_tasks_for_user(app_state.current_user.id)
        
        # Get filtered tasks and update the display
        filtered_tasks = self.get_filtered_tasks()
        self.populate_tasks(filtered_tasks)
    
    def get_selected_task(self):
        """
        Get the Task object for the selected row.
  
        """
        # Get selected item from Treeview
        selection = self.tree.selection()
        if not selection:
            return None
        
        # Get the task_id from the selected item
        task_id_str = selection[0]
        task_id = int(task_id_str)
        
        # Find the corresponding Task in app_state.tasks
        for task in app_state.tasks:
            if task.id == task_id:
                return task
        
        return None
    
    def _on_add_task(self):
        """Handle Add Task button."""
        TaskForm(self, on_save=self.refresh_tasks)
    
    def _on_edit_task(self):
        """Handle Edit Task button."""
        # Get selected task
        selected_task = self.get_selected_task()
        
        # If a task is selected, open TaskForm in edit mode
        if selected_task:
            TaskForm(self, task=selected_task, on_save=self.refresh_tasks)
    
    def _on_delete_task(self):
        """Handle Delete Task button."""

        selected_task = self.get_selected_task()
        
        # If a task is selected, delete it
        if selected_task:
            # Delete from database
            delete_task(selected_task.id)
            
            
            app_state.tasks.remove(selected_task)
            
            # Refresh the view
            self.populate_tasks(app_state.tasks)
    
    def _on_complete_task(self):
        """Handle Complete Task button."""

        selected_task = self.get_selected_task()
        
        # If a task is selected, mark it as completed
        if selected_task:
            # Mark task as completed 
            selected_task.mark_completed()
            
            # Update in database
            update_task(selected_task)
            
            # Refresh the view
            self.refresh_tasks()
    
    def _on_refresh(self):
        """Handle Refresh button."""
        self.refresh_tasks()
    
    def _on_reports(self):
        """Handle Reports button."""
        ReportsView(self)

