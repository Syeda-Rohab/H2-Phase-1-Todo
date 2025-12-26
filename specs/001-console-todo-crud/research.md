# Research: Console CRUD Todo Application

**Feature**: 001-console-todo-crud
**Date**: 2025-12-26
**Status**: Complete

## Technical Decisions

### 1. CLI Argument Parsing

**Decision**: Use `argparse` (Python standard library)

**Rationale**:
- Built into Python 3.13+ (no external dependencies)
- Provides automatic help generation
- Handles subcommands naturally (add, list, update, etc.)
- Type validation and error messages included
- Industry standard for Python CLI applications

**Alternatives Considered**:
- **Click**: Popular but requires external dependency (violates minimal dependencies principle)
- **Fire**: Automatic but less explicit control over argument validation
- **Manual sys.argv parsing**: Too error-prone and verbose

### 2. Data Persistence Format

**Decision**: JSON file with atomic writes

**Rationale**:
- Human-readable for debugging and hackathon demonstration
- Native Python support via `json` module (no dependencies)
- Simple schema matches Task model structure
- Atomic writes prevent data corruption on crashes
- Easy to validate and version

**Implementation Pattern**:
```python
# Write to temp file, then atomic rename
with open('tasks.tmp.json', 'w') as f:
    json.dump(tasks, f, indent=2)
os.replace('tasks.tmp.json', 'tasks.json')  # Atomic operation
```

**Alternatives Considered**:
- **SQLite**: Overkill for single-user console app, adds complexity
- **Pickle**: Not human-readable, security concerns
- **CSV**: Poor support for nested data (description field with commas)

### 3. Task ID Generation

**Decision**: Sequential integer IDs starting from 1

**Rationale**:
- User-friendly (easy to type in console)
- Predictable for testing and demonstration
- Simple implementation (max(existing_ids) + 1)
- Matches specification examples in acceptance criteria

**Implementation**:
```python
def generate_next_id(tasks: list[Task]) -> int:
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1
```

**Alternatives Considered**:
- **UUID**: Too long for console typing, overkill for single-user
- **Hash-based**: Non-sequential confuses users
- **Auto-incrementing counter file**: Extra complexity, atomic issues

### 4. Timestamp Format

**Decision**: ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)

**Rationale**:
- Specified in FR-001 and Task entity definition
- Sortable as strings
- Human-readable
- Standard Python support via `datetime.isoformat()`
- Timezone-aware (UTC recommended)

**Implementation**:
```python
from datetime import datetime, timezone

created_at = datetime.now(timezone.utc).isoformat()
```

**Alternatives Considered**:
- **Unix timestamp**: Less readable in list display
- **Custom format**: Reinventing standards

### 5. Error Handling Strategy

**Decision**: Explicit exception handling with user-friendly messages

**Rationale**:
- FR-008 requires clear error messages
- Constitution V requires no silent failures
- Helps hackathon judges understand robustness

**Error Categories**:
1. **Invalid Arguments**: Missing title, invalid ID format
2. **Not Found**: Task ID doesn't exist
3. **File I/O**: Corrupted JSON, permission denied
4. **Validation**: Empty title, invalid data types

**Implementation Pattern**:
```python
try:
    task_id = int(id_str)
except ValueError:
    print(f"Error: Invalid ID '{id_str}'. Must be a number.")
    sys.exit(1)
```

**Alternatives Considered**:
- **Silent failures**: Violates constitution
- **Stack traces**: Unprofessional for end users
- **Log files**: Overkill for console app

### 6. List Display Format

**Decision**: Tabular format with status symbols

**Rationale**:
- Clear visual hierarchy
- Status symbols (✓/○) are intuitive
- Aligns with FR-002 requirements
- Professional appearance for judges

**Format**:
```
ID | Status | Title                  | Description            | Created
1  | ✓      | Design mockups         | Create wireframes...   | 2025-12-26 14:30
2  | ○      | Review code            | PR #123 needs review   | 2025-12-26 15:45
```

**Alternatives Considered**:
- **JSON output**: Machine-readable but ugly for humans
- **Simple list**: Harder to scan quickly
- **Rich formatting (colors)**: Requires external dependency

### 7. File Structure and Imports

**Decision**: Modular structure with clear separation of concerns

**Rationale**:
- Task model in `src/models/task.py` (data)
- Business logic in `src/todo_app.py` (operations)
- CLI interface in `src/main.py` (presentation)
- Follows single responsibility principle

**Module Responsibilities**:
- `task.py`: Task dataclass, validation, serialization
- `todo_app.py`: CRUD operations, file I/O, ID generation
- `main.py`: Argument parsing, command dispatch, output formatting

**Alternatives Considered**:
- **Single file**: Simple but violates clean code principles
- **Over-engineered (repositories, services)**: Overkill for scope

### 8. Type Hints Strategy

**Decision**: Full type hints on all public APIs and dataclasses

**Rationale**:
- Constitution V requires type hints
- Catches bugs early
- Serves as documentation
- Professional code quality for judges

**Example**:
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Task:
    id: int
    title: str
    description: str
    completed: bool
    created_at: str

def add_task(title: str, description: str) -> Task:
    ...
```

**Alternatives Considered**:
- **Partial typing**: Inconsistent, defeats purpose
- **Runtime validation (Pydantic)**: External dependency

## Best Practices Summary

1. **Prefer standard library** over external dependencies
2. **Atomic file operations** for data integrity
3. **Explicit error handling** with user-friendly messages
4. **Type hints everywhere** for safety and documentation
5. **Modular structure** following single responsibility
6. **ISO 8601 timestamps** for consistency
7. **Sequential integer IDs** for usability
8. **Tabular console output** for readability

## Implementation Readiness

All technical decisions resolved. No blocking unknowns remain. Ready for Phase 1 (data model and contracts).
