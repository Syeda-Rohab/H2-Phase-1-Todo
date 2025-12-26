"""Task model for todo items."""

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Dict, Any


@dataclass
class Task:
    """Represents a todo task.

    Attributes:
        id: Unique identifier for the task
        title: Short description of the task
        description: Detailed description of the task
        completed: Whether the task is completed
        created_at: ISO 8601 timestamp of task creation
    """

    id: int
    title: str
    description: str
    completed: bool
    created_at: str

    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary for JSON serialization.

        Returns:
            Dictionary representation of the task
        """
        return asdict(self)

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'Task':
        """Create task from dictionary (JSON deserialization).

        Args:
            data: Dictionary containing task data

        Returns:
            Task instance
        """
        return Task(
            id=int(data['id']),
            title=str(data['title']),
            description=str(data['description']),
            completed=bool(data['completed']),
            created_at=str(data['created_at'])
        )

    def validate(self) -> None:
        """Validate task data meets constraints.

        Raises:
            ValueError: If validation fails
        """
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")
        if len(self.title) > 500:
            raise ValueError("Title cannot exceed 500 characters")
        if len(self.description) > 2000:
            raise ValueError("Description cannot exceed 2000 characters")
        if self.id <= 0:
            raise ValueError("ID must be positive integer")


def create_task(task_id: int, title: str, description: str) -> Task:
    """Factory function to create a new task with auto-generated timestamp.

    Args:
        task_id: Unique identifier for the task
        title: Task title
        description: Task description

    Returns:
        New Task instance with UTC timestamp

    Raises:
        ValueError: If validation fails
    """
    now = datetime.now(timezone.utc).isoformat()
    task = Task(
        id=task_id,
        title=title.strip(),
        description=description.strip(),
        completed=False,
        created_at=now
    )
    task.validate()
    return task
