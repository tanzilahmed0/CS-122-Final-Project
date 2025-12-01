CS-122-FINAL-PROJECT/
├─ README.md
├─ requirements.txt
├─ run.py                      # Entry point: launches the GUI app
├─ taskmaster/                 # Python package
│  ├─ __init__.py
│  ├─ config.py                # Paths, DB file name, app constants
│  ├─ models/                  # Core domain models (OOP)
│  │  ├─ __init__.py
│  │  ├─ base.py               # BaseModel, shared behavior (inheritance)
│  │  ├─ user.py               # User, StudentUser, AdminUser
│  │  └─ task.py               # Task, CourseTask, PersonalTask
│  ├─ storage/                 # Persistence: file/DB access
│  │  ├─ __init__.py
│  │  ├─ db.py                 # DatabaseManager: SQLite connection + schema
│  │  └─ repositories.py       # UserRepository, TaskRepository (CRUD)
│  ├─ services/                # Business logic layer (no GUI code)
│  │  ├─ __init__.py
│  │  ├─ app_state.py          # AppState: current user, in-memory caches
│  │  ├─ user_service.py       # Login, registration, user management
│  │  ├─ task_service.py       # Task CRUD, filtering, sorting
│  │  └─ report_service.py     # Visual report data: stats & summaries
│  ├─ gui/                     # Tkinter GUI
│  │  ├─ __init__.py
│  │  ├─ app.py                # Tk root, main loop, screen switching
│  │  ├─ login_view.py         # Login / profile selection screen
│  │  ├─ main_window.py        # Dashboard with to-do list + filters
│  │  ├─ task_form_view.py     # Add/edit task dialog/window
│  │  └─ reports_view.py       # Visual report screen (charts, stats)
│  ├─ utils/                   # Helpers
│  │  ├─ __init__.py
│  │  ├─ validators.py         # Validation helpers for input
│  │  └─ logging_config.py     # Logging setup
│  └─ logs/
│     └─ app.log               # Runtime logging output
└─ data/
   ├─ taskmaster.db            # SQLite DB file (created at runtime)
   └─ schema.sql               # Optional: schema definition/seeding
