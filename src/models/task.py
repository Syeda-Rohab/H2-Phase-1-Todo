"""Task model for todo items."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    """Represents a todo task.

    Attributes:
        id: Unique identifier for the task
        title: Short description of the task
        description: Detailed description of the task
        completed: Whether the task is completed
        created: ISO 8601 timestamp of task creation
    """

    id: int
    title: str
    description: str
    completed: bool
    created: str

    @classmethod
    def create(cls, task_id: int, title: str, description: str) -> "Task":
        """Create a new task with auto-generated timestamp.

        Args:
            task_id: Unique identifier for the task
            title: Task title
            description: Task description

        Returns:
            New Task instance
        """
        timestamp = datetime.now().isoformat()
        return cls(
            id=task_id,
            title=title,
            description=description,
            completed=False,
            created=timestamp
        )

    def to_dict(self) -> dict:
        """Convert task to dictionary for JSON serialization.

        Returns:
            Dictionary representation of the task
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created": self.created
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        """Create task from dictionary.

        Args:
            data: Dictionary containing task data

        Returns:
            Task instance
        """
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            completed=data["completed"],
            created=data["created"]
        )
