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