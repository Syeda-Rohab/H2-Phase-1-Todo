# The Evolution of Todo

A spec-driven console todo application built with Python 3.13+ and UV package manager.

## Project Overview

This project demonstrates professional Python development practices using:
- **Spec-Driven Development** with Spec-Kit Plus methodology
- **UV Package Manager** for fast, reliable dependency management
- **Clean Code** principles with type hints and comprehensive error handling
- **Console-only interface** for simplicity and focus

## Features

The Evolution of Todo implements 5 core CRUD operations:

1. ✅ **Add Task** - Create new tasks with title and description
2. ✅ **View Tasks** - List all tasks with status indicators
3. ✅ **Update Task** - Modify task title and description
4. ✅ **Delete Task** - Remove tasks by ID
5. ✅ **Mark Complete/Incomplete** - Toggle task completion status

## Setup Instructions

### Prerequisites

- **Python 3.13+** installed
- **UV package manager** installed

### Install UV

If you don't have UV installed, install it using:

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Project Setup

1. **Clone or navigate to the project directory**:
   ```bash
   cd "Todo H2"
   ```

2. **Create a virtual environment with UV**:
   ```bash
   uv venv
   ```

3. **Activate the virtual environment**:
   ```bash
   # On Windows
   .venv\Scripts\activate

   # On macOS/Linux
   source .venv/bin/activate
   ```

4. **Install dependencies** (currently none for runtime, optional dev tools):
   ```bash
   uv pip install -e ".[dev]"
   ```

## Usage

### Add a Task

```bash
python -m src.main add "Buy milk" "Go to store for milk"
```

**Output:**
```
✓ Task added successfully! ID: 1
```

### List All Tasks

```bash
python -m src.main list
```

**Output:**
```
ID    | Title                          | Status       | Created
----------------------------------------------------------------------
1     | Buy milk                       | ✗ Incomplete | 2025-12-26T14:30:00
```

### Update a Task

```bash
python -m src.main update 1 "Buy bread" "Bread from bakery"
```

**Output:**
```
[OK] Task 1 updated successfully!
```

### Delete a Task

```bash
python -m src.main delete 1
```

**Output:**
```
[OK] Task 1 deleted successfully!
```

### Mark Task Complete

```bash
python -m src.main complete 1
```

**Output:**
```
[OK] Task 1 marked as complete!
```

### Mark Task Incomplete

```bash
python -m src.main incomplete 1
```

**Output:**
```
[OK] Task 1 marked as incomplete!
```

## Project Structure

```
Todo H2/
├── Constitution.txt           # Project governance rules
├── CLAUDE.md                  # AI agent guidance
├── README.md                  # This file
├── pyproject.toml            # UV project configuration
├── specs_history/             # All feature specifications
│   ├── add_task.spec.md      # ✅ Implemented
│   ├── view_tasks.spec.md    # ✅ Implemented
│   ├── update_task.spec.md   # ✅ Implemented
│   ├── delete_task.spec.md   # ✅ Implemented
│   └── complete_task.spec.md # ✅ Implemented
├── src/                       # Source code
│   ├── __init__.py
│   ├── main.py               # Console entrypoint
│   ├── todo_app.py           # Core application logic
│   └── models/
│       ├── __init__.py
│       └── task.py           # Task data model
├── tasks.json                # Task data storage (auto-created)
└── .specify/                 # Spec-Kit Plus framework
    ├── memory/
    │   └── constitution.md   # Detailed project principles
    └── templates/            # Spec templates
```

## Data Persistence

Tasks are automatically saved to `tasks.json` in the project root. The file uses atomic writes to prevent corruption and will be created automatically on first use.

**Example `tasks.json`:**
```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Buy milk",
      "description": "Go to store for milk",
      "completed": false,
      "created": "2025-12-26T14:30:00"
    }
  ],
  "next_id": 2
}
```

## Development Workflow

This project follows **Spec-Driven Development**:

1. Read specification from `specs_history/`
2. Implement ONLY that feature (no scope creep)
3. Test manually via console commands
4. Commit with reference to spec file
5. Move to next specification

See `Constitution.txt` or `.specify/memory/constitution.md` for complete development principles.

## Type Checking

Run type checking with mypy:

```bash
uv run mypy src/
```

## Code Formatting

Format code with black:

```bash
uv run black src/
```

## Constitution & Principles

This project is governed by a formal constitution defining:
- 7 Core Principles (Feature Completeness, Data Model, CRUD Operations, Persistence, Type Safety, Console Interface, Spec-Driven Workflow)
- Technology Stack requirements
- Project structure standards
- Development workflow
- Governance and compliance

See `.specify/memory/constitution.md` for the complete constitution.

## License

Educational project - see project documentation for details.

## Current Status

**Version**: 1.0.0
**Status**: ✅ COMPLETE - All features implemented!
**Completed Features**: 5/5 (100%)
- ✅ Add Task
- ✅ View Tasks
- ✅ Update Task
- ✅ Delete Task
- ✅ Mark Complete/Incomplete

All features tested and working with full data persistence!
