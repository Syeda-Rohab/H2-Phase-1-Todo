"""Console entrypoint for The Evolution of Todo application."""

import sys
from src.todo_app import TodoApp


def main() -> None:
    """Main entry point for the console application."""
    if len(sys.argv) < 2:
        print("[ERROR] No command provided")
        print("\nUsage:")
        print('  python -m src.main add "Title" "Description"')
        print("  python -m src.main list")
        print('  python -m src.main update <ID> "New Title" "New Description"')
        print("  python -m src.main delete <ID>")
        print("  python -m src.main complete <ID>")
        print("  python -m src.main incomplete <ID>")
        sys.exit(1)

    command = sys.argv[1].lower()
    app = TodoApp()

    try:
        if command == "add":
            handle_add(app, sys.argv[2:])
        elif command == "list":
            handle_list(app)
        elif command == "update":
            handle_update(app, sys.argv[2:])
        elif command == "delete":
            handle_delete(app, sys.argv[2:])
        elif command == "complete":
            handle_complete(app, sys.argv[2:])
        elif command == "incomplete":
            handle_incomplete(app, sys.argv[2:])
        else:
            print(f"[ERROR] Unknown command '{command}'")
            sys.exit(1)
    except ValueError as e:
        print(f"[ERROR] {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR] {e}")
        sys.exit(1)


def handle_add(app: TodoApp, args: list) -> None:
    """Handle the add command.

    Args:
        app: TodoApp instance
        args: Command arguments [title, description]
    """
    if len(args) < 2:
        raise ValueError("Both title and description are required")

    title = args[0]
    description = args[1]

    task = app.add_task(title, description)
    print(f"[OK] Task added successfully! ID: {task.id}")


def handle_list(app: TodoApp) -> None:
    """Handle the list command.

    Args:
        app: TodoApp instance
    """
    tasks = app.list_tasks()

    if not tasks:
        print("No tasks found.")
        return

    # Print header
    print(f"{'ID':<5} | {'Title':<30} | {'Status':<14} | {'Created':<20}")
    print("-" * 74)

    # Print tasks
    for task in tasks:
        status = "[X] Complete" if task.completed else "[ ] Incomplete"
        title = task.title[:27] + "..." if len(task.title) > 30 else task.title
        created = task.created_at[:19]  # Strip microseconds
        print(f"{task.id:<5} | {title:<30} | {status:<14} | {created:<20}")


def handle_update(app: TodoApp, args: list) -> None:
    """Handle the update command.

    Args:
        app: TodoApp instance
        args: Command arguments [id, title, description]
    """
    if len(args) < 3:
        raise ValueError("Update requires: <ID> <Title> <Description>")

    try:
        task_id = int(args[0])
    except ValueError:
        raise ValueError("Invalid task ID: must be an integer")

    title = args[1]
    description = args[2]

    task = app.update_task(task_id, title, description)
    print(f"[OK] Task {task.id} updated successfully!")


def handle_delete(app: TodoApp, args: list) -> None:
    """Handle the delete command.

    Args:
        app: TodoApp instance
        args: Command arguments [id]
    """
    if len(args) < 1:
        raise ValueError("Task ID is required")

    try:
        task_id = int(args[0])
    except ValueError:
        raise ValueError("Invalid task ID: must be an integer")

    app.delete_task(task_id)
    print(f"[OK] Task {task_id} deleted successfully!")


def handle_complete(app: TodoApp, args: list) -> None:
    """Handle the complete command.

    Args:
        app: TodoApp instance
        args: Command arguments [id]
    """
    if len(args) < 1:
        raise ValueError("Task ID is required")

    try:
        task_id = int(args[0])
    except ValueError:
        raise ValueError("Invalid task ID: must be an integer")

    task = app.complete_task(task_id)
    print(f"[OK] Task {task.id} marked as complete!")


def handle_incomplete(app: TodoApp, args: list) -> None:
    """Handle the incomplete command.

    Args:
        app: TodoApp instance
        args: Command arguments [id]
    """
    if len(args) < 1:
        raise ValueError("Task ID is required")

    try:
        task_id = int(args[0])
    except ValueError:
        raise ValueError("Invalid task ID: must be an integer")

    task = app.incomplete_task(task_id)
    print(f"[OK] Task {task.id} marked as incomplete!")


if __name__ == "__main__":
    main()
