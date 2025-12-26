# CLI Command Contracts: Console CRUD Todo Application

**Feature**: 001-console-todo-crud
**Date**: 2025-12-26
**Interface Type**: Command-Line Interface (CLI)

## Command Interface Overview

All commands are invoked via:
```bash
python -m src.main <command> [arguments]
```

**Common Behavior**:
- Exit code 0 on success
- Exit code 1 on error
- UTF-8 output encoding
- Errors printed to stderr
- Success output printed to stdout

---

## Command: `add`

**Purpose**: Create a new task with title and description

### Syntax
```bash
python -m src.main add <title> [description]
```

### Parameters

| Parameter | Type | Required | Constraints | Description |
|-----------|------|----------|-------------|-------------|
| `title` | string | Yes | 1-500 chars | Task title (quoted if contains spaces) |
| `description` | string | No | 0-2000 chars | Task details (quoted if contains spaces, defaults to "") |

### Success Response
```
Task added: #<ID> <title>
```

**Example**:
```bash
$ python -m src.main add "Design mockups" "Create wireframes for login page"
Task added: #1 Design mockups
```

### Error Responses

| Error Case | Exit Code | Message |
|------------|-----------|---------|
| Missing title | 1 | `Error: Title is required. Usage: add <title> [description]` |
| Empty title | 1 | `Error: Title cannot be empty` |
| Title too long (>500 chars) | 1 | `Error: Title cannot exceed 500 characters` |
| Description too long (>2000 chars) | 1 | `Error: Description cannot exceed 2000 characters` |

### Side Effects
- Generates new unique ID (max existing ID + 1)
- Sets `completed` to `False`
- Sets `created_at` to current UTC timestamp
- Appends task to `data/tasks.json`

---

## Command: `list`

**Purpose**: Display all tasks with formatting

### Syntax
```bash
python -m src.main list
```

### Parameters
None

### Success Response (tasks exist)
```
ID | Status | Title                  | Description                    | Created
1  | ✓      | Design mockups         | Create wireframes for login... | 2025-12-26 14:30
2  | ○      | Review code            |                                | 2025-12-26 15:45
```

**Format Rules**:
- Header row with column names
- Status: `✓` for completed=true, `○` for completed=false
- Long descriptions truncated with `...` (display first 30 chars)
- Timestamp formatted as `YYYY-MM-DD HH:MM` (UTC, no seconds)
- Columns aligned for readability

### Success Response (no tasks)
```
No tasks found.
```

### Error Responses

| Error Case | Exit Code | Message |
|------------|-----------|---------|
| Corrupted data file | 0 | `Warning: Corrupted data file. Showing empty list.` (then shows empty) |
| Permission denied | 1 | `Error: Cannot read task file. Check permissions.` |

### Side Effects
None (read-only operation)

---

## Command: `update`

**Purpose**: Modify task title and/or description by ID

### Syntax
```bash
python -m src.main update <id> --title <new_title> --description <new_description>
python -m src.main update <id> --title <new_title>
python -m src.main update <id> --description <new_description>
```

### Parameters

| Parameter | Type | Required | Constraints | Description |
|-----------|------|----------|-------------|-------------|
| `id` | integer | Yes | > 0 | Task ID to update |
| `--title` | string | No* | 1-500 chars | New title (quoted if contains spaces) |
| `--description` | string | No* | 0-2000 chars | New description (quoted if contains spaces) |

*At least one of `--title` or `--description` must be provided.

### Success Response
```
Task #<ID> updated.
```

**Example**:
```bash
$ python -m src.main update 1 --title "Design UI mockups"
Task #1 updated.
```

### Error Responses

| Error Case | Exit Code | Message |
|------------|-----------|---------|
| Missing ID | 1 | `Error: Task ID is required. Usage: update <id> --title <title> --description <desc>` |
| Invalid ID format | 1 | `Error: Invalid ID '<value>'. Must be a number.` |
| Task not found | 1 | `Error: Task #<ID> not found.` |
| No fields provided | 1 | `Error: At least one of --title or --description must be provided.` |
| Title too long | 1 | `Error: Title cannot exceed 500 characters` |
| Description too long | 1 | `Error: Description cannot exceed 2000 characters` |

### Side Effects
- Updates specified fields in task
- Preserves unspecified fields (partial update)
- Does NOT modify `id`, `completed`, or `created_at`
- Saves changes to `data/tasks.json`

---

## Command: `delete`

**Purpose**: Permanently remove a task by ID

### Syntax
```bash
python -m src.main delete <id>
```

### Parameters

| Parameter | Type | Required | Constraints | Description |
|-----------|------|----------|-------------|-------------|
| `id` | integer | Yes | > 0 | Task ID to delete |

### Success Response
```
Task #<ID> deleted.
```

**Example**:
```bash
$ python -m src.main delete 3
Task #3 deleted.
```

### Error Responses

| Error Case | Exit Code | Message |
|------------|-----------|---------|
| Missing ID | 1 | `Error: Task ID is required. Usage: delete <id>` |
| Invalid ID format | 1 | `Error: Invalid ID '<value>'. Must be a number.` |
| Task not found | 1 | `Error: Task #<ID> not found.` |

### Side Effects
- Removes task from task list
- Remaining task IDs are NOT renumbered
- Saves changes to `data/tasks.json`

---

## Command: `complete`

**Purpose**: Mark a task as completed

### Syntax
```bash
python -m src.main complete <id>
```

### Parameters

| Parameter | Type | Required | Constraints | Description |
|-----------|------|----------|-------------|-------------|
| `id` | integer | Yes | > 0 | Task ID to mark complete |

### Success Response
```
Task #<ID> marked as complete.
```

**Example**:
```bash
$ python -m src.main complete 1
Task #1 marked as complete.
```

### Error Responses

| Error Case | Exit Code | Message |
|------------|-----------|---------|
| Missing ID | 1 | `Error: Task ID is required. Usage: complete <id>` |
| Invalid ID format | 1 | `Error: Invalid ID '<value>'. Must be a number.` |
| Task not found | 1 | `Error: Task #<ID> not found.` |

### Side Effects
- Sets `completed` to `True`
- Idempotent: running on already-completed task succeeds (no error)
- Saves changes to `data/tasks.json`

---

## Command: `incomplete`

**Purpose**: Mark a task as incomplete (undo completion)

### Syntax
```bash
python -m src.main incomplete <id>
```

### Parameters

| Parameter | Type | Required | Constraints | Description |
|-----------|------|----------|-------------|-------------|
| `id` | integer | Yes | > 0 | Task ID to mark incomplete |

### Success Response
```
Task #<ID> marked as incomplete.
```

**Example**:
```bash
$ python -m src.main incomplete 1
Task #1 marked as incomplete.
```

### Error Responses

| Error Case | Exit Code | Message |
|------------|-----------|---------|
| Missing ID | 1 | `Error: Task ID is required. Usage: incomplete <id>` |
| Invalid ID format | 1 | `Error: Invalid ID '<value>'. Must be a number.` |
| Task not found | 1 | `Error: Task #<ID> not found.` |

### Side Effects
- Sets `completed` to `False`
- Idempotent: running on already-incomplete task succeeds (no error)
- Saves changes to `data/tasks.json`

---

## General Error Handling

### Unknown Command
```bash
$ python -m src.main foobar
Error: Unknown command 'foobar'.
Available commands: add, list, update, delete, complete, incomplete
```
Exit code: 1

### No Command Provided
```bash
$ python -m src.main
Error: No command provided.
Usage: python -m src.main <command> [arguments]
Available commands: add, list, update, delete, complete, incomplete
```
Exit code: 1

### Help Flag
```bash
$ python -m src.main --help
Usage: python -m src.main <command> [arguments]

Commands:
  add <title> [description]              Create a new task
  list                                   Display all tasks
  update <id> --title T --description D  Update task by ID
  delete <id>                            Delete task by ID
  complete <id>                          Mark task as complete
  incomplete <id>                        Mark task as incomplete

Examples:
  python -m src.main add "Buy milk" "Get 2% milk from store"
  python -m src.main list
  python -m src.main complete 1
```
Exit code: 0

---

## Implementation Notes

### Argument Parsing
Use `argparse` with subcommands:
```python
parser = argparse.ArgumentParser(prog='python -m src.main')
subparsers = parser.add_subparsers(dest='command', required=True)

# Add command
add_parser = subparsers.add_parser('add')
add_parser.add_argument('title', type=str)
add_parser.add_argument('description', type=str, nargs='?', default='')

# List command
list_parser = subparsers.add_parser('list')

# Update command
update_parser = subparsers.add_parser('update')
update_parser.add_argument('id', type=int)
update_parser.add_argument('--title', type=str, required=False)
update_parser.add_argument('--description', type=str, required=False)

# ... etc for delete, complete, incomplete
```

### Output Formatting
- Use f-strings for consistent message formatting
- Use `textwrap.shorten()` for description truncation
- Use `datetime.fromisoformat()` for timestamp parsing
- Use UTF-8 encoding for status symbols (✓/○)

### Error Message Consistency
All error messages follow pattern:
```
Error: <What went wrong>. <Optional usage hint>
```

All warning messages follow pattern:
```
Warning: <What's wrong but not fatal>. <What happened instead>
```
