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
        
        Args:
            parent: Parent widget
            on_login_success: Callback function to call after successful login
        """
        super().__init__(parent)
        self.on_login_success = on_login_success
        
        self._build_ui()
    
    def _build_ui(self):
        """Build the login UI layout."""
        # Label
        label = tk.Label(self, text="Enter username:", font=("Arial", 14))
        label.pack(pady=20)
        
        # Username entry
        self.username_entry = tk.Entry(self, font=("Arial", 12), width=30)
        self.username_entry.pack(pady=10)
        
        # Login button
        login_button = tk.Button(self, text="Login", font=("Arial", 12), command=self._on_login_click)
        login_button.pack(pady=20)
    
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
        
        # Set current user in app state
        app_state.current_user = user
        
        # Call success callback if provided
        if self.on_login_success:
            self.on_login_success()

