# Small helpers: validation + basic logging setup

import logging
from datetime import datetime

# Configure basic logging
logging.basicConfig(level=logging.INFO)

# Create module-level logger
logger = logging.getLogger("taskmaster")


def parse_due_date(text: str):
    """
    Convert string input into a datetime or None.
    
    Args:
        text: Date string in format MM/DD/YYYY
        
    Returns:
        datetime object or None if invalid/empty
    """
    if not text or not text.strip():
        return None
    
    try:
        return datetime.strptime(text.strip(), "%m/%d/%Y")
    except ValueError:
        return None

