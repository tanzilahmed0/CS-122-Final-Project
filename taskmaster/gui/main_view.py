# Main task list view (CRUD + filters)

import tkinter as tk
from tkinter import ttk
from taskmaster.storage import get_tasks_for_user
from taskmaster.app_state import app_state


class MainView(tk.Frame):
    """Main task list view with CRUD operations and filters."""
    
    def __init__(self, parent):
        """
        Initialize MainView.
        
        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        self._build_ui()
    
    def _build_ui(self):
        """Build the main view UI layout."""
        # Top frame for filters
        filter_frame = tk.Frame(self)
        filter_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Status filter
        tk.Label(filter_frame, text="Status:").pack(side=tk.LEFT, padx=5)
        self.status_filter = ttk.Combobox(filter_frame, values=["All", "Pending", "Completed"], state="readonly", width=15)
        self.status_filter.set("All")
        self.status_filter.pack(side=tk.LEFT, padx=5)
        
        # Priority filter
        tk.Label(filter_frame, text="Priority:").pack(side=tk.LEFT, padx=5)
        self.priority_filter = ttk.Combobox(filter_frame, values=["All", "Low", "Medium", "High"], state="readonly", width=15)
        self.priority_filter.set("All")
        self.priority_filter.pack(side=tk.LEFT, padx=5)
        
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
        
        # Buttons
        tk.Button(button_frame, text="Add Task", command=self._on_add_task).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Edit Task", command=self._on_edit_task).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Task", command=self._on_delete_task).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Complete Task", command=self._on_complete_task).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Refresh", command=self._on_refresh).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Reports", command=self._on_reports).pack(side=tk.LEFT, padx=5)
    
    def populate_tasks(self, tasks):
        """
        Display a list of tasks in the Treeview.
        
        Args:
            tasks: List of Task objects to display
        """
        # Clear existing rows
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Insert new rows
        for task in tasks:
            # Format due date
            due_date_str = task.due_date.strftime("%Y-%m-%d") if task.due_date else ""
            
            # Insert row with task data
            self.tree.insert("", tk.END, iid=str(task.id), values=(
                task.title,
                due_date_str,
                task.priority,
                task.status,
                task.category or ""
            ))
    
    def refresh_tasks(self):
        """Reload tasks from database and update the view."""
        # Reload tasks from database
        app_state.tasks = get_tasks_for_user(app_state.current_user.id)
        
        # Update the display
        self.populate_tasks(app_state.tasks)
    
    def _on_add_task(self):
        """Handle Add Task button (no logic yet)."""
        pass
    
    def _on_edit_task(self):
        """Handle Edit Task button (no logic yet)."""
        pass
    
    def _on_delete_task(self):
        """Handle Delete Task button (no logic yet)."""
        pass
    
    def _on_complete_task(self):
        """Handle Complete Task button (no logic yet)."""
        pass
    
    def _on_refresh(self):
        """Handle Refresh button."""
        self.refresh_tasks()
    
    def _on_reports(self):
        """Handle Reports button (no logic yet)."""
        pass

