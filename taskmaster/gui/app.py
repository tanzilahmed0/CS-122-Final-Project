# Tk root, main loop, screen switching

import tkinter as tk
from taskmaster.storage import db_manager, get_tasks_for_user
from taskmaster.gui.login_view import LoginView
from taskmaster.gui.main_view import MainView
from taskmaster.app_state import app_state


def main():
    """Main entry point for the GUI application."""
    # Initialize database before starting GUI
    db_manager.init_db()
    
    # Create the root window
    root = tk.Tk()
    root.title("Task Master")
    
    # Define callback for successful login
    def on_login_success():
        # Load tasks for the current user
        app_state.tasks = get_tasks_for_user(app_state.current_user.id)
        
        # Hide/destroy LoginView
        login_view.pack_forget()
        login_view.destroy()
        
        # Create and display MainView
        main_view = MainView(root)
        main_view.pack(fill=tk.BOTH, expand=True)
        
        # Populate tasks in MainView
        main_view.populate_tasks(app_state.tasks)
    
    # Create and display LoginView
    login_view = LoginView(root, on_login_success=on_login_success)
    login_view.pack(fill=tk.BOTH, expand=True)
    
    # Start the main event loop
    root.mainloop()

