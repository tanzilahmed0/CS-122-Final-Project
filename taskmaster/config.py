# App-wide constants, DB path

import os

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "taskmaster.db")

# Task constants
PRIORITIES = ["Low", "Medium", "High"]
STATUSES = ["Pending", "Completed"]
CATEGORIES = ["School", "Work", "Personal"]

