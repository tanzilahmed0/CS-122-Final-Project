from taskmaster.storage import db_manager, create_user, get_user_by_username, create_task
from taskmaster.models import User, Task
from datetime import datetime

# Initialize database
db_manager.init_db()

# Create or get a test user
username = "testuser"
user = get_user_by_username(username)
if user is None:
    user = User(username=username, display_name="Test User")
    create_user(user)
    print(f"Created new user: {user}")
else:
    print(f"Using existing user: {user}")

# Create a test task
task = Task(
    user_id=user.id,
    title="Test Task from Script",
    description="This is a test task created by script",
    due_date=datetime(2025, 12, 15),
    priority="High",
    status="Pending",
    category="Work"
)
create_task(task)
print(f"Created task: {task.title} (ID: {task.id})")

