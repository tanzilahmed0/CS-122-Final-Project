CS-122-FINAL-PROJECT/
├─ README.md
├─ requirements.txt
├─ run.py                     # Entry point: starts the GUI app
├─ data/
│  └─ taskmaster.db           # SQLite DB (created at runtime)
└─ taskmaster/                # Main package
   ├─ __init__.py
   ├─ config.py               # App-wide constants, DB path
   ├─ models.py               # BaseModel, User, Task (OOP)
   ├─ storage.py              # DatabaseManager + simple CRUD helper functions
   ├─ app_state.py            # Global in-memory state (current user, tasks)
   ├─ reports.py              # Simple functions to compute report stats
   ├─ utils.py                # Small helpers: validation + basic logging setup
   └─ gui/                    # All GUI code
      ├─ __init__.py
      ├─ app.py               # Tk root, navigation between views
      ├─ login_view.py        # Login screen (multi-user)
      ├─ main_view.py         # Main task list view (CRUD + filters)
      ├─ task_form.py         # Add/Edit task dialog
      └─ reports_view.py      # Simple stats/visual report screen


## File Responsibilities

### config.py
Holds DB path, priorities/status constants, and categories.

### models.py
Defines BaseModel, User, Task. Handles validation and encapsulation.

### storage.py
SQLite logic: initializing DB and CRUD functions for users and tasks.

### app_state.py
Holds the global in-memory state: current_user and tasks.

### reports.py
Computes simple statistics: count_by_status and count_by_category.

### utils.py
Helper functions like parse_due_date and logging setup.

### gui/app.py
Creates the Tk root window, initializes DB, and switches between screens.

### gui/login_view.py
Username entry screen for basic multi-user login.

### gui/main_view.py
Main task list UI with CRUD, filters, and buttons.

### gui/task_form.py
Popup dialog to add or edit a task.

### gui/reports_view.py
Simple popup showing stats about tasks.
