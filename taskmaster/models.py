# BaseModel, User, Task (OOP)

from datetime import datetime


class BaseModel:
    """Base class for shared fields and behavior."""
    
    def __init__(self, id=None, created_at=None, updated_at=None):
        """
        Initialize base model with common fields.
        
        Args:
            id: Unique identifier (set by database)
            created_at: Creation timestamp
            updated_at: Last update timestamp
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
        
        Returns:
            dict: Dictionary containing id, created_at, updated_at
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
        
        Args:
            username: Username (will be normalized)
            display_name: Display name for the user
            id: Unique identifier (set by database)
            created_at: Creation timestamp
            updated_at: Last update timestamp
        """
        super().__init__(id, created_at, updated_at)
        self.username = username.strip().lower() if username else ""
        self.display_name = display_name
    
    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', display_name='{self.display_name}')"
    
    def __str__(self):
        return f"{self.display_name} (@{self.username})"

