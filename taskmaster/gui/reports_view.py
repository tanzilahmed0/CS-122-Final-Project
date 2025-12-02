# Visual report screen (charts, stats)

import tkinter as tk
from tkinter import ttk
from taskmaster.app_state import app_state
from taskmaster.reports import count_by_status, count_by_category


class ReportsView(tk.Toplevel):
    """Simple popup window showing task statistics."""
    
    def __init__(self, parent):
        """
        Initialize ReportsView.
        
        Args:
            parent: Parent widget
        """
        super().__init__(parent)
        self.title("Task Reports")
        self.geometry("400x300")
        
        self._build_ui()
    
    def _build_ui(self):
        """Build the reports UI and display statistics."""
        # Title
        tk.Label(self, text="Task Statistics", font=("Arial", 16, "bold")).pack(pady=20)
        
        # Get statistics
        status_counts = count_by_status(app_state.tasks)
        category_counts = count_by_category(app_state.tasks)
        
        # Status section
        tk.Label(self, text="By Status:", font=("Arial", 12, "bold")).pack(pady=(10, 5), anchor=tk.W, padx=20)
        
        for status, count in status_counts.items():
            tk.Label(self, text=f"  {status}: {count}", font=("Arial", 10)).pack(anchor=tk.W, padx=40)
        
        # If no statuses, show message
        if not status_counts:
            tk.Label(self, text="  No tasks", font=("Arial", 10)).pack(anchor=tk.W, padx=40)
        
        # Category section
        tk.Label(self, text="By Category:", font=("Arial", 12, "bold")).pack(pady=(20, 5), anchor=tk.W, padx=20)
        
        for category, count in category_counts.items():
            category_name = category if category else "(No Category)"
            tk.Label(self, text=f"  {category_name}: {count}", font=("Arial", 10)).pack(anchor=tk.W, padx=40)
        
        # If no categories, show message
        if not category_counts:
            tk.Label(self, text="  No tasks", font=("Arial", 10)).pack(anchor=tk.W, padx=40)
        
        # Close button
        tk.Button(self, text="Close", font=("Arial", 10), command=self.destroy, width=10).pack(pady=20)

