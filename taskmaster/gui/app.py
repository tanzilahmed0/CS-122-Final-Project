# Tk root, main loop, screen switching

import tkinter as tk
from taskmaster.storage import db_manager
from taskmaster.gui.login_view import LoginView
from taskmaster.app_state import app_state


def main():
    """Main entry point for the GUI application."""
    # Initialize database before starting GUI
    db_manager.init_db()
    
    # Create the root window
    root = tk.Tk()
    root.title("Task Master")
    
    # Temporary callback to verify login
    def on_login_success():
        print(f"Logged in: {app_state.current_user}")
    
    # Create and display LoginView
    login_view = LoginView(root, on_login_success=on_login_success)
    login_view.pack(fill=tk.BOTH, expand=True)
    
    # Start the main event loop
    root.mainloop()

