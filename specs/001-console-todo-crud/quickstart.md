# Quickstart: Console CRUD Todo Application

**Feature**: 001-console-todo-crud | **Date**: 2025-12-26

## Implementation Order

1. **Task Model** (`src/models/task.py`) - Dataclass with 5 fields
2. **Storage** (`src/todo_app.py`) - load_tasks(), save_tasks(), generate_next_id()
3. **CRUD Logic** (`src/todo_app.py`) - add, get, update, delete, complete operations
4. **CLI** (`src/main.py`) - argparse with subcommands and output formatting

## Key Patterns

**Atomic Write**:
```python
os.replace('data/tasks.tmp.json', 'data/tasks.json')
```

**ID Generation**:
```python
return max(task.id for task in tasks) + 1 if tasks else 1
```

**Error Handling**:
```python
if not task:
    print(f"Error: Task #{id} not found.", file=sys.stderr)
    sys.exit(1)
```

## Testing
Run manual tests from contracts/cli-commands.md covering all success and error cases.

## Definition of Done
- All 5 commands work (add, list, update, delete, complete/incomplete)
- Data persists across restarts
- Output matches contract format
- Type hints on all functions
- No external dependencies
