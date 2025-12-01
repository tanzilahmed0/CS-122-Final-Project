# DatabaseManager + simple CRUD helper functions

import sqlite3
import os
from taskmaster.config import DB_PATH, DATA_DIR


class DatabaseManager:
    """Handles SQLite database connections and operations."""
    
    def __init__(self, db_path: str):
        """
        Initialize DatabaseManager with a database path.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
    
    def get_connection(self):
        """
        Get a connection to the SQLite database.
        
        Returns:
            sqlite3.Connection: Database connection object
        """
        return sqlite3.connect(self.db_path)
    
    def init_db(self):
        """
        Initialize the database by creating tables if they don't exist.
        Ensures the data directory exists first.
        """
        # Ensure data directory exists
        os.makedirs(DATA_DIR, exist_ok=True)
        
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                display_name TEXT NOT NULL,
                created_at TIMESTAMP NOT NULL,
                updated_at TIMESTAMP NOT NULL
            )
        """)
        
        # Create tasks table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT NOT NULL,
                description TEXT,
                due_date TIMESTAMP,
                priority TEXT NOT NULL,
                status TEXT NOT NULL,
                category TEXT,
                created_at TIMESTAMP NOT NULL,
                updated_at TIMESTAMP NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        
        conn.commit()
        conn.close()


# Module-level database manager instance
db_manager = DatabaseManager(DB_PATH)


def create_user(user):
    """
    Insert a new user into the database.
    
    Args:
        user: User object to insert
        
    Returns:
        User: The user object with id set from database
    """
    conn = db_manager.get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO users (username, display_name, created_at, updated_at)
        VALUES (?, ?, ?, ?)
    """, (user.username, user.display_name, user.created_at, user.updated_at))
    
    user.id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    return user


def get_user_by_username(username):
    """
    Fetch a user by username.
    
    Args:
        username: Username to search for
        
    Returns:
        User object if found, None otherwise
    """
    from taskmaster.models import User
    
    conn = db_manager.get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, username, display_name, created_at, updated_at
        FROM users
        WHERE username = ?
    """, (username.strip().lower(),))
    
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return User(
            username=row[1],
            display_name=row[2],
            id=row[0],
            created_at=row[3],
            updated_at=row[4]
        )
    
    return None


def create_task(task):
    """
    Insert a new task into the database.
    
    Args:
        task: Task object to insert
        
    Returns:
        Task: The task object with id set from database
    """
    conn = db_manager.get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO tasks (user_id, title, description, due_date, priority, status, category, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (task.user_id, task.title, task.description, task.due_date, 
          task.priority, task.status, task.category, task.created_at, task.updated_at))
    
    task.id = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    return task


def get_tasks_for_user(user_id):
    """
    Load all tasks for a given user.
    
    Args:
        user_id: ID of the user whose tasks to retrieve
        
    Returns:
        list[Task]: List of Task objects for the user
    """
    from taskmaster.models import Task
    
    conn = db_manager.get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, user_id, title, description, due_date, priority, status, category, created_at, updated_at
        FROM tasks
        WHERE user_id = ?
    """, (user_id,))
    
    rows = cursor.fetchall()
    conn.close()
    
    tasks = []
    for row in rows:
        task = Task(
            user_id=row[1],
            title=row[2],
            description=row[3],
            due_date=row[4],
            priority=row[5],
            status=row[6],
            category=row[7],
            id=row[0],
            created_at=row[8],
            updated_at=row[9]
        )
        tasks.append(task)
    
    return tasks


def update_task(task):
    """
    Update an existing task in the database.
    
    Args:
        task: Task object with updated values (must have id set)
    """
    conn = db_manager.get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE tasks
        SET user_id = ?, title = ?, description = ?, due_date = ?, 
            priority = ?, status = ?, category = ?, updated_at = ?
        WHERE id = ?
    """, (task.user_id, task.title, task.description, task.due_date,
          task.priority, task.status, task.category, task.updated_at, task.id))
    
    conn.commit()
    conn.close()


def delete_task(task_id):
    """
    Delete a task by id.
    
    Args:
        task_id: ID of the task to delete
    """
    conn = db_manager.get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        DELETE FROM tasks
        WHERE id = ?
    """, (task_id,))
    
    conn.commit()
    conn.close()

