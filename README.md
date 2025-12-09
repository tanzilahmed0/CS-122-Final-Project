# CS-122 Final Project

TaskMaster - Task Management Application

A simple GUI-based task management system built with Python and Tkinter, featuring multi-user support, task CRUD operations, filtering, and reporting capabilities.

## How to Run

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python run.py
   ```

3. **Using the Application**
   - Enter a username on the login screen (creates a new user if it doesn't exist)
   - Add, edit, delete, and complete tasks
   - Filter tasks by status and priority
   - View task statistics in the Reports view

The application uses SQLite for data persistence. The database file will be automatically created at `data/taskmaster.db` on first run.

