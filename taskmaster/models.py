# BaseModel, User, Task (OOP)

from datetime import datetime
from taskmaster import config


class BaseModel:
    """Base class for shared fields and behavior."""
    
    def __init__(self, id=None, created_at=None, updated_at=None):
        """
        Initialize base model with common fields.
        
        """
        self.id = id
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()
    
    def touch(self):
        """Update the updated_at timestamp to current time."""
        self.updated_at = datetime.utcnow()
    
    def to_dict(self):
        """
        Return a dictionary representation of base fields.
        """
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }


class User(BaseModel):
    """Represent a user profile."""
    
    def __init__(self, username, display_name, id=None, created_at=None, updated_at=None):
        """
        Initialize a User.
        
        """
        super().__init__(id, created_at, updated_at)
        self.username = username.strip().lower() if username else ""
        self.display_name = display_name
    
    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', display_name='{self.display_name}')"
    
    def __str__(self):
        return f"{self.display_name} (@{self.username})"


class Task(BaseModel):
    """Represent an individual task."""
    
    def __init__(self, user_id, title, description, due_date, priority, status, category,
                 id=None, created_at=None, updated_at=None):
        """
        Initialize a Task.
        
        """
        super().__init__(id, created_at, updated_at)
        self.user_id = user_id
        self.title = title
        self.description = description
        self.due_date = due_date
        
        # Validate priority
        self.priority = priority if priority in config.PRIORITIES else "Medium"
        
        # Validate status
        self.status = status if status in config.STATUSES else "Pending"
        
        self.category = category
    
    def mark_completed(self):
        """Mark this task as completed and update timestamp."""
        self.status = "Completed"
        self.touch()
    
    def is_overdue(self, now):
        """
        Check if this task is overdue.
     
        """
        if self.status == "Completed":
            return False
        if self.due_date is None:
            return False
        return self.due_date < now

