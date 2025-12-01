# DatabaseManager + simple CRUD helper functions

import sqlite3
from taskmaster.config import DB_PATH


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


# Module-level database manager instance
db_manager = DatabaseManager(DB_PATH)

