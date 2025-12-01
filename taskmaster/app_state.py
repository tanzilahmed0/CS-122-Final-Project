# Global in-memory state (current user, tasks)


class AppState:
    """Central in-memory state container for the application."""
    
    def __init__(self):
        """Initialize AppState with empty/None values."""
        self.current_user = None
        self.tasks = []


# Module-level app state instance
app_state = AppState()

