"""Core todo application logic."""

import json
from pathlib import Path
from typing import List, Optional
from src.models.task import Task


class TodoApp:
    """Main todo application class handling task operations."""

    DATA_FILE = Path("tasks.json")

    def __init__(self) -> None:
        """Initialize the todo application."""
        self.tasks: List[Task] = []
        self.next_id: int = 1
        self._load_tasks()

    def _load_tasks(self) -> None:
        """Load tasks from JSON file."""
        if not self.DATA_FILE.exists():
            return

        try:
            with open(self.DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data.get("tasks", [])]
                self.next_id = data.get("next_id", 1)
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Data file corrupted: {e}")

    def _save_tasks(self) -> None:
        """Save tasks to JSON file with atomic write."""
        data = {
            "tasks": [task.to_dict() for task in self.tasks],
            "next_id": self.next_id
        }

        # Atomic write: write to temp file then rename
        temp_file = self.DATA_FILE.with_suffix('.tmp')
        try:
            with open(temp_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            temp_file.replace(self.DATA_FILE)
        except Exception as e:
            if temp_file.exists():
                temp_file.unlink()
            raise IOError(f"Failed to save tasks: {e}")

    def add_task(self, title: str, description: str) -> Task:
        """Add a new task.

        Args:
            title: Task title (must be non-empty)
            description: Task description (must be non-empty)

        Returns:
            The created Task instance

        Raises:
            ValueError: If title or description is empty
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        if not description or not description.strip():
            raise ValueError("Description cannot be empty")

        task = Task.create(self.next_id, title.strip(), description.strip())
        self.tasks.append(task)
        self.next_id += 1
        self._save_tasks()

        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            Task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self) -> List[Task]:
        """Get all tasks.

        Returns:
            List of all tasks
        """
        return self.tasks.copy()

    def update_task(self, task_id: int, title: str, description: str) -> Task:
        """Update a task's title and description.

        Args:
            task_id: ID of the task to update
            title: New title (must be non-empty)
            description: New description (must be non-empty)

        Returns:
            The updated Task instance

        Raises:
            ValueError: If task not found, or title/description is empty
        """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        if not description or not description.strip():
            raise ValueError("Description cannot be empty")

        task = self.get_task(task_id)
        if task is None:
            raise ValueError(f"Task ID {task_id} not found")

        task.title = title.strip()
        task.description = description.strip()
        self._save_tasks()

        return task

    def delete_task(self, task_id: int) -> None:
        """Delete a task by ID.

        Args:
            task_id: ID of the task to delete

        Raises:
            ValueError: If task not found
        """
        task = self.get_task(task_id)
        if task is None:
            raise ValueError(f"Task ID {task_id} not found")

        self.tasks.remove(task)
        self._save_tasks()

    def complete_task(self, task_id: int) -> Task:
        """Mark a task as complete.

        Args:
            task_id: ID of the task to mark complete

        Returns:
            The updated Task instance

        Raises:
            ValueError: If task not found
        """
        task = self.get_task(task_id)
        if task is None:
            raise ValueError(f"Task ID {task_id} not found")

        task.completed = True
        self._save_tasks()

        return task

    def incomplete_task(self, task_id: int) -> Task:
        """Mark a task as incomplete.

        Args:
            task_id: ID of the task to mark incomplete

        Returns:
            The updated Task instance

        Raises:
            ValueError: If task not found
        """
        task = self.get_task(task_id)
        if task is None:
            raise ValueError(f"Task ID {task_id} not found")

        task.completed = False
        self._save_tasks()

        return task
