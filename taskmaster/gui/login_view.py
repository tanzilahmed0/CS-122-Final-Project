# Login / profile selection screen

import tkinter as tk
from tkinter import ttk
from taskmaster.storage import get_user_by_username, create_user
from taskmaster.models import User
from taskmaster.app_state import app_state


class LoginView(tk.Frame):
    """Login screen for basic multi-user login."""
    
    def __init__(self, parent, on_login_success=None):
        """
        Initialize LoginView.
        
        """
        super().__init__(parent)
        self.on_login_success = on_login_success
        
        self._build_ui()
    
    def _build_ui(self):
        """Build the login UI layout."""
        # Add spacing at top
        tk.Frame(self, height=60).pack()
        
        # Title
        title = tk.Label(self, text="Task Master", font=("Arial", 24, "bold"))
        title.pack(pady=10)
        
        # Add spacing
        tk.Frame(self, height=40).pack()
        
        # Label
        label = tk.Label(self, text="Enter username:", font=("Arial", 14, "bold"))
        label.pack(pady=15)
        
        # Username entry
        self.username_entry = tk.Entry(self, font=("Arial", 14), width=30, relief=tk.SOLID, bd=2)
        self.username_entry.pack(pady=10, ipady=10)
        
        # Add spacing
        tk.Frame(self, height=20).pack()
        
        # Login button
        login_button = tk.Button(
            self, 
            text="Login", 
            font=("Arial", 14, "bold"), 
            command=self._on_login_click,
            relief=tk.RAISED,
            bd=3,
            bg="#4CAF50",
            fg="black",
            activebackground="#45a049"
        )
        login_button.pack(pady=10, ipadx=50, ipady=12)
    
    def _on_login_click(self):
        """Handle login button click."""
        # Read username from entry
        username = self.username_entry.get().strip()
        
        if not username:
            return
        
        # Try to get existing user
        user = get_user_by_username(username)
        
        # If user doesn't exist, create new user
        if user is None:
            user = User(username=username, display_name=username.capitalize())
            create_user(user)
        
  
        app_state.current_user = user
        
        # Call success callback if provided
        if self.on_login_success:
            self.on_login_success()

